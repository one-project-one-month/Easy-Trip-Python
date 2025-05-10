from dotenv import load_dotenv
import os 
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

model = init_chat_model("groq:llama3-70b-8192")

prompt_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful assistant and you can manage what things we should bring when we go trips based on {{Location}} and {{Days}}.'),
    ('human', "What should I bring, I be going to {location} within {days}"
)])

generate_output = prompt_template | model 

print(generate_output.invoke({"location":"Bagan","days":"5/10/2025 to 5/15/2025"}))