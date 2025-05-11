from dotenv import load_dotenv 
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from langchain_groq import ChatGroq
from typing_extensions import TypedDict, Annotated, List
from langgraph.graph.message import add_messages 
from langgraph.graph import StateGraph , START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import AIMessage

load_dotenv()

@tool 
def weather_check(query:str) -> str:
    """Return only weather condition based on user's location"""
    return DuckDuckGoSearchRun().invoke(query)

model = ChatGroq(model_name="llama-3.3-70b-versatile")

tools = [weather_check]
model_bind_tools = model.bind_tools(tools)

class State(TypedDict):
    messages: Annotated[List[AIMessage], add_messages]

def generating_model(state:State):
    return {"messages": [model_bind_tools.invoke(state['messages'])]}

workflow = StateGraph(State)
workflow.add_node("generating_model", generating_model)
workflow.add_node("tools", ToolNode(tools))

workflow.add_edge(START, "generating_model")
workflow.add_conditional_edges('generating_model', tools_condition)
workflow.add_edge("tools", "generating_model")

graph = workflow.compile()

result = graph.invoke({'messages': "What should i bring if i want to travel Bagan in 5/11/2025 to 5/15/2025"})
#print(result)
print(result['messages'][-1].content)

