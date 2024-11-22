from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import OllamaLLM
from pydantic import BaseModel
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from langchain_openai import ChatOpenAI

load_dotenv()

llms = []

llm_openai_3_5 = ChatOpenAI(model_name="gpt-3.5-turbo")
llms.append(llm_openai_3_5)
llm_openai_4 = ChatOpenAI(model_name="gpt-4")
llms.append(llm_openai_4)
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

allowed_origins = [
    "http://localhost:5173"
]

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


@app.get("/")
def home():
    return llms


def get_llm_by_model(m: str):
    return next((llm for llm in llms if (hasattr(llm, 'model_name') and llm.model_name == m) or
                 (hasattr(llm, 'model') and llm.model == m)), None)


def answer_prompt_of_model(m: str, prompt_text: str):
    this_llm = get_llm_by_model(m)
    if this_llm is not None:
        output = this_llm.invoke(prompt_text)
        return output
    else:
        return "There exists no LLM or LLM Instance of this model"


@app.post("/models/postreq")
async def answer_prompt(request: PromptRequest):
    m = request.llm
    prompt = request.prompt_text
    return answer_prompt_of_model(m, prompt)
