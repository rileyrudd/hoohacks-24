from fastapi import FastAPI, HTTPException
import os, json
import asyncio
import re
# import langchain_helper as lch
import langchainHuggingface as lhf
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow origins (replace * with specific origins if needed)
origins = ["*"]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


def get_env_variable(var_name: str) -> str:
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"Environment variable '{var_name}' not found.")
    return value


try:
    USE_ASYNC = os.getenv("USE_ASYNC", "False").lower() == "true"
    if USE_ASYNC:
        print("Async project used")
        os.environ['PREDICTIONGUARD_TOKEN'] = "q1VuOjnffJ3NO2oFN8Q9m8vghYc84ld13jaqdF7E"
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

    mode = "async" if USE_ASYNC else "sync"
except ValueError as e:
    raise HTTPException(status_code=500, detail=str(e))
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))



def extract_json_from_string(input_string):
    # Regular expression pattern to find JSON
    print(input_string)
    pattern = r'({[^}]*})'

    # Search for JSON using the pattern
    match = re.search(pattern, input_string)
    if match:
        json_part = match.group(1)
        # Parse the JSON
        try:
            json_data = json.loads(json_part)
            return json_data
        except json.JSONDecodeError as e:
            print("Error decoding JSON:", e)
            return None
    else:
        print("No JSON found in the input string.")
        return None

@app.get("/advise")
def quick_response():
    response = extract_json_from_string(lhf.get_analysis())
    if response is None:
        return {"message": "Something went wrong. Let's retry."}
    else:
        return response
    # print(lhf.langchain_agent())
    # return json.loads(lhf.langchain_agent())

class Message(BaseModel):
    message: str


@app.post("/chat")
def quick_chat(message: Message):
    raw_response = lhf.get_response(message.message)
    response = extract_json_from_string(lhf.get_response(message.message))
    if response is None or "":
        split_text = raw_response.split('"advice":')
        advice_text = split_text[1]
        advice_text = advice_text[:-1]
        return {"advice": advice_text}
    else:
        return response