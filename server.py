# server.py

from fastapi import FastAPI
from pydantic import BaseModel, Field
from blockAgent import BlockAgentDad
import time
app = FastAPI()

class InputBlock(BaseModel):
    action: str
    character: str
    target: str
    cards: list
    probability: float = Field(..., ge=0.0, le=1.0)  # Ensure probability is between 0 and 1
    intermediate_steps: list

block_agent = BlockAgentDad()

@app.post("/get_result")
def get_result(inputs_block: InputBlock):
    inputs = inputs_block.dict()
    # Convert probability to percentage as expected by the class
    inputs["probability"] = int(inputs["probability"] * 100)
    
    start_time = time.time()
    result = block_agent.get_result(inputs)
    end_time = time.time()
    
    time_taken = end_time - start_time
    
    return {"result": result, "time_taken": time_taken}

# Run the server with: uvicorn server:app --reload
