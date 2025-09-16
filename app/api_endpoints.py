# api_endpoints.py
"""
FastAPI endpoint and model definitions for Maximo API Project MVP
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from app.db.connection import SQLServerConnection
from app.services.query_builder import build_query

router = APIRouter()

# --- Models ---

class ReportInfo(BaseModel):
    id: str
    name: str
    description: str

class ReportParameter(BaseModel):
    name: str
    type: str
    required: bool
    description: str

class RunReportRequest(BaseModel):
    parameters: Dict[str, Any]

class RunReportResponse(BaseModel):
    columns: List[str]
    rows: List[List[Any]]

# --- Endpoints ---

@router.get("/reports", response_model=List[ReportInfo])
def list_reports():
    # Example: Only one report for MVP
    return [
        ReportInfo(id="work_order_summary", name="Work Order Summary", 
                   description="Advanced work order report")
    ]


@router.get("/reports/{report_id}/parameters", response_model=List[ReportParameter])
def get_report_parameters(report_id: str):
    # Example: Return static parameters for MVP
    if report_id == "work_order_summary":
        return [
            ReportParameter(name="work_order_num", type="string", required=False, description="work order number"),
            ReportParameter(name="status", type="string", required=False, description="work order status"),
            ReportParameter(name="worktype", type="string", required=False, description="work order type (Enum: CM, PM, EM, CAP, ENV, SAF, OTH)"),
            ReportParameter(name="assignedownergroup", type="string", required=False, description="assigned owner group (Enum: FWNAE, FWNAST, FWNAST1, FWNCAD, FWNCCM, FWNCI, FWNCS, FWNCSM, FWNCSR, FWNCSS, FWNDCQ, FWNEN2, FWNFMOP, FWNHR, FWNHSE, FWNITOP, FWNLC1, FWNLCP1, FWNLCP2, FWNLCP3, FWNLCP4, FWNMC1, FWNMCS, FWNMDC, FWNMET, FWNMICR1, FWNMICR2, FWNMNTSCH, FWNMOS, FWNPA1, FWNPE, FWNPS, FWNPSC, FWNPSM, FWNPSP, FWNPSP1, FWNPSP2, FWNPSP3, FWNPSP4, FWNPSP5, FWNPSP6, FWNPSP7, FWNQACA, FWNQACL, FWNQACP, FWNQALO, FWNQAMI, FWNQAOP, FWNQAOP1, FWNQAW, FWNQCAST, FWNQOI, FWNRECMGT, FWNRXM, FWNSQA, FWNVAL, FWNWSM)"),
            # ...add more fields as needed
        ]
    raise HTTPException(status_code=404, detail="Report not found")


@router.post("/reports/{report_id}/run", response_model=RunReportResponse)

def run_report(report_id: str, request: RunReportRequest):
    import logging
    if report_id == "work_order_summary":
        query, params = build_query(request.parameters)
        try:
            with SQLServerConnection() as conn:
                conn.raw_cursor.execute(query, params)
                rows = conn.raw_cursor.fetchall()
                columns = [column[0] for column in conn.raw_cursor.description]
                data = []
                for row_idx, row in enumerate(rows):
                    safe_row = []
                    for col_idx, value in enumerate(row):
                        try:
                            # Try to decode bytes, else convert to string
                            if isinstance(value, bytes):
                                safe_row.append(value.decode('utf-8', errors='replace'))
                            else:
                                safe_row.append(str(value))
                        except Exception as e:
                            logging.error(f"Error decoding row {row_idx}, column {columns[col_idx]}: {e}")
                            safe_row.append(f"<decode error: {e}>")
                    data.append(safe_row)
                return RunReportResponse(
                    columns=columns,
                    rows=data
                )
        except Exception as e:
            logging.error(f"Database or decoding error: {e}")
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
    raise HTTPException(status_code=404, detail="Report not found")
