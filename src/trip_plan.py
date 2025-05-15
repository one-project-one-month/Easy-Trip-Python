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
Return only a JSON object with key (Day are depends on the user start date and end date)
{{
  "title": "",
  "description": "",

  "transportation": {{
    "local_pass": "",
    "recommandation_info": [
      "",
      "",
      ""
    ]
  }},

  "accomodation": {{
    "suggested_area": "",
    "hotel_option": [
      {{
        "name": "",
        "price_per_night": 0,
        "link": ""
      }},
      {{
        "name": "",
        "price_per_night": 0,
        "link": ""
      }}
    ]
  }},

  "day_by_day_plan": [
    {{
      "day": 1,
      "date": "",
      "title": "",
      "place": "",
      "description": "",
      "activities": [
        "",
        "",
        "",
        ""
      ],
      "estimated_day_budget": 0
    }},
    {{
      "day": 2,
      "date": "",
      "title": "",
      "place": "",
      "description": "",
      "activities": [
        "",
        "",
        "",
        ""
      ],
      "estimated_day_budget": 0
    }},
    {{
      "day": 3,
      "date": "",
      "title": "",
      "place": "",
      "description": "",
      "activities": [
        ""
      ],
      "estimated_day_budget": 0
    }}
  ],

  "budget_breakdown": {{
    "accommodation": 0,
    "food": 0,
    "transport": 0,
    "activities": 0,
    "total_estimated": 0,
    "remaining_budget": 0,
    "recommandation": ""
  }},

  "cultural_sensitivity_tips": [
    "",
    "",
    "",
    ""
  ],

  "emergency_tips": {{
    "nearest_clinic": "",
    "tourist_police": "",
    "general_emergency": "",
    "local_assistance": ""
  }},

  "conflict_with_festival": false,

  "notes": [
    ""
  ]
}}
"""

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system),
    ("human", "{input}")
])

app = FastAPI(title="Thing You Should Bring API", version = "1.0")

add_routes(app, prompt_template | model , path= "/trip") 

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)