from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class State(BaseModel):
    name: str
    abbreviation: str

@app.get("/states")
async def get_states():
    return [{"name": "Alabama", "abbreviation": "AL"}, {"name": "Alaska", "abbreviation": "AK"}]

