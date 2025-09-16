
from fastapi import FastAPI
from app.api_endpoints import router as report_router
from app.db.connection import SQLServerConnection
from app.models.work_order_input import WorkOrderInput
from app.services.query_builder import build_query


app = FastAPI(title="Maximo API")

# Include the new report endpoints
app.include_router(report_router)

@app.get("/")
def read_root():
    return {"message": "Maximo API is running"}


@app.post("/workorders")
def get_work_orders(input: WorkOrderInput):
    query = build_query(input)
    with SQLServerConnection() as conn:
        conn.raw_cursor.execute(query)
        results = conn.raw_cursor.fetchall()
    return {"data": results}

