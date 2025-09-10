# Pydantic models for work order input
from pydantic import BaseModel

class WorkOrderInput(BaseModel):
    work_order_num: Optional[List[str]] = None
    status: Optional[str] = None
    site_id: List[str]
    istask: int
    woclass: str
r
