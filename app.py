from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_ollama import OllamaLLM
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

app = FastAPI(middleware=middleware)


@app.get("/")
def home():
    return llms


@app.get("/models/{m}")
def get_llm_by_model(m: str):
    return next((llm for llm in llms if (hasattr(llm, 'model_name') and llm.model_name == m) or
                 (hasattr(llm, 'model') and llm.model == m)), None)


@app.get("/models/{m}/{prompt_text}")
def answer_prompt_of_model(m: str, prompt_text: str):
    this_llm = get_llm_by_model(m)
    if this_llm is not None:
        output = this_llm.invoke(prompt_text)
        return output
    else:
        return "There exists no LLM or LLM Instance of this model"
