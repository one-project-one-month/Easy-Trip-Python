from dotenv import load_dotenv
import os 
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from fastapi import FastAPI
import uvicorn

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

model = init_chat_model("groq:llama-3.3-70b-versatile")

system = """
Return only a JSON object with key "thingsYouShouldBring", whose values are relevant items a traveler should bring when going to a specific location for a specific number of days. Make the list detailed and adapted to the location and length of travel."""

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system),
    ("human", "Which things should we bring in order to go to {destination} with {group_type} within {start_day} to {end_day}"),
])

app = FastAPI(title="Thing You Should Bring API", version = "1.0")

add_routes(app, prompt_template | model , path= "/things") 

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)