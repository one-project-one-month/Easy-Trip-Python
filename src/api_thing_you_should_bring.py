from dotenv import load_dotenv
import os 
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
import uvicorn

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

model = init_chat_model("ollama:tinyllama:1.1b")

prompt_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful assistant and you can manage what things we should bring when we go trips based on {{Location}} and {{Days}}.'),
    ('human', "What should I bring, I be going to {location} within {days}"
)])


app = FastAPI(title="Thing You Should Bring API", version = "1.0")

add_routes(app, prompt_template | model , path= "/things") 

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)