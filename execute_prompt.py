from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def execute_prompt(prompt):
    try:
        model = ChatOpenAI(model_name="gpt-4o-mini")
        return model.invoke(prompt)
    except Exception as e:
        return str(e)
