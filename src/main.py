from dotenv import load_dotenv
import os 
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

model = init_chat_model("groq:llama-3.3-70b-versatile", temperature = 0.5)

system = """
Return only a JSON object with key "thingsYouShouldBring", whose values are relevant items a traveler should bring when going to a specific location for a specific number of days. Make the list detailed and adapted to the location and length of travel."""

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system),
    ("human", "Which things should we bring in order to go to {destination} with {group_type} within {start_day} to {end_day}")
])

#prompt_template.invoke({"location":"Bagan","days":"5/10/2025 to 5/15/2025"})

generate_output = prompt_template | model 

result = generate_output.invoke({"destination":"Yangon", "group_type": "Family", "start_day": "5/11/2025", 'end_day': '15/11/2025'})

print(result.content)
