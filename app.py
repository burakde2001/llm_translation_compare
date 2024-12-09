from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import OllamaLLM
from pydantic import BaseModel
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI

from rag.init_pinecone import vectorstore

load_dotenv()

llms = []

llm_openai_3_5 = ChatOpenAI(model_name="gpt-3.5-turbo")
llms.append(llm_openai_3_5)
llm_openai_4 = ChatOpenAI(model_name="gpt-4")
llms.append(llm_openai_4)

llm_eval = ChatOpenAI(model_name="gpt-3.5-turbo")

allowed_origins = [
    "http://localhost:5173"
]

#'ollama serve' MUSS in einer separaten Powershell vorher ausgeführt werden
llm_llama_3_2 = OllamaLLM(model="llama3.2")
llms.append(llm_llama_3_2)
llm_leo = OllamaLLM(model="hf.co/TheBloke/leo-hessianai-13B-chat-GGUF")
llms.append(llm_leo)
llm_disco = OllamaLLM(model="hf.co/TheBloke/DiscoLM_German_7b_v1-GGUF")
llms.append(llm_disco)
llm_sauerkraut = OllamaLLM(model="cyberwald/llama-3.1-sauerkrautlm-8b-instruct")
llms.append(llm_sauerkraut)
llm_mistral = OllamaLLM(model="mistral")
llms.append(llm_mistral)


llm_gemini = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
llms.append(llm_gemini)

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )
]

class PromptRequest(BaseModel):
    llm: str
    prompt_text: str


app = FastAPI(middleware=middleware)

code_prompt_eval_DE = PromptTemplate(
    template="Bewerte die Antwort <{answer}> auf den Prompt <{p}>",
    input_variables=["answer, p"]
)

sequence_DE = code_prompt_eval_DE | llm_eval

def run_chain_eval_DE(answer, p):
    result = sequence_DE.invoke({"answer": answer, "p": p})
    return result


@app.get("/")
def home():
    return llms


def get_llm_by_model(m: str):
    return next((llm for llm in llms if (hasattr(llm, 'model_name') and llm.model_name == m) or
          (hasattr(llm, 'model') and llm.model == m)), None)


@app.get("/eval")
def get_eval_llm():
    return llm_eval


def answer_prompt_of_model(m: str, prompt_text: str):
    this_llm = get_llm_by_model(m)
    if this_llm is not None:
        output = this_llm.invoke(prompt_text)
        return output
    else:
        return "There exists no LLM or LLM Instance of this model"


def evaluate_answer_of_prompt(m: str, prompt_text: str):
    this_llm = get_llm_by_model(m)
    if this_llm is not None:
        answer = this_llm.invoke(prompt_text)
        return run_chain_eval_DE(answer, prompt_text)
    else:
        return "There exists no LLM or LLM Instance of this model"


def query_pinecone(query_text, top_k=40):
    docs = vectorstore.similarity_search(query_text, k=top_k)
    return docs


@app.post("/models/postreq")
async def answer_prompt(request: PromptRequest):
    m = request.llm
    prompt = request.prompt_text
    return answer_prompt_of_model(m, prompt)


@app.post("/models/posteval")
async def eval_prompt(request: PromptRequest):
    m = request.llm
    prompt = request.prompt_text
    return evaluate_answer_of_prompt(m, prompt)


@app.post("/rag/models/postreq")
async def answer_prompt(request: PromptRequest):
    m = request.llm
    prompt = request.prompt_text
    context = []
    results = query_pinecone(prompt)
    for doc in results:
        context.append(doc.page_content)
    llm_prompt = f"""
    prompt: {prompt}

    Generate an answer to the given prompt. For the answer, consider including information given in the following context. Don't repeat the prompt within the answer.
    context: {context}
    """
    return answer_prompt_of_model(m, llm_prompt)
