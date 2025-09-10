from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

# Define the Pydantic model
class WorkOrderInput(BaseModel):
    work_order_num: Optional[List[str]] = None
    status: Optional[str] = None
    site_id: List[str]
    istask: int
    woclass: str

# Create FastAPI app
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Maximo API is running"}

@app.post("/workorder")
def create_workorder(input_data: WorkOrderInput):
    return {
        "message": "Work order input received",
        "data": input_data.model_dump()
    }

