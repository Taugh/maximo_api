from fastapi import FastAPI
from app.db.connection import get_db_connection
from app.models.work_order_input import WorkOrderInput
from app.services.query_builder import build_query

app = FastAPI(title="Maximo API")

@app.get("/")
def read_root():
    return {"message": "Maximo API is running"}

@app.post("/workorders")
def get_work_orders(input: WorkOrderInput):
    conn = get_db_connection()
    query = build_query(input)
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return {"data": results}

