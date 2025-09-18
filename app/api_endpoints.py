# api_endpoints.py
"""
FastAPI endpoint and model definitions for Maximo API Project MVP
"""

from fastapi import APIRouter, HTTPException, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from app.models.work_order_fields import WORK_ORDER_FIELDS
# --- CORS Setup ---
def add_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

from pydantic import BaseModel
from typing import List, Dict, Any
import io
import xlsxwriter
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



# Existing JSON endpoint remains
@router.post("/reports/{report_id}/run", response_model=RunReportResponse)

def run_report(report_id: str, request: RunReportRequest):
    import logging
    if report_id == "work_order_summary":
        import pprint
        print("Request parameters:")
        pprint.pprint(request.parameters)
        selected_fields = request.parameters.get('fields')
        allowed_fields = [f['parameter_name'] for f in WORK_ORDER_FIELDS]
        # Validate selected fields
        if selected_fields:
            invalid = [f for f in selected_fields if f not in allowed_fields]
            if invalid:
                raise HTTPException(status_code=400, detail=f"Invalid field(s): {', '.join(invalid)}")
        # If not provided, use all fields
        if not selected_fields:
            select_fields = [
                f"wo.{f['field_name']}" if f['field_name'] != 'assetnum' else "a.assetnum" for f in WORK_ORDER_FIELDS
            ]
        else:
            select_fields = []
            for f in WORK_ORDER_FIELDS:
                if f['parameter_name'] in selected_fields:
                    if f['field_name'] == 'assetnum':
                        select_fields.append("a.assetnum")
                    elif f['field_name'] == 'assetdesc':
                        select_fields.append("a.description AS assetdesc")
                    else:
                        select_fields.append(f"wo.{f['field_name']}")
        # Pagination
        page = int(request.parameters.get('page', 1))
        page_size = int(request.parameters.get('page_size', 100))
        offset = (page - 1) * page_size
        from app.services.query_builder import build_query
        query, params = build_query(request.parameters, select_fields=select_fields)
        print(f"SQL Query: {query}")
        print(f"Parameters: {params}")
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

# New XLSX endpoint
@router.post("/reports/{report_id}/run_xlsx")

def run_report_xlsx(report_id: str, request: RunReportRequest):
    import logging
    if report_id == "work_order_summary":
        selected_fields = request.parameters.get('fields')
        allowed_fields = [f['parameter_name'] for f in WORK_ORDER_FIELDS]
        if selected_fields:
            invalid = [f for f in selected_fields if f not in allowed_fields]
            if invalid:
                raise HTTPException(status_code=400, detail=f"Invalid field(s): {', '.join(invalid)}")
        if not selected_fields:
            select_fields = [
                f"wo.{f['field_name']}" if f['field_name'] != 'assetnum' else "a.assetnum" for f in WORK_ORDER_FIELDS
            ]
        else:
            select_fields = []
            for f in WORK_ORDER_FIELDS:
                if f['parameter_name'] in selected_fields:
                    if f['field_name'] == 'assetnum':
                        select_fields.append("a.assetnum")
                    elif f['field_name'] == 'assetdesc':
                        select_fields.append("a.description AS assetdesc")
                    else:
                        select_fields.append(f"wo.{f['field_name']}")
        # Use the same query builder logic as JSON endpoint
        from app.services.query_builder import build_query
        query, params = build_query(request.parameters, select_fields=select_fields)
        print(f"SQL Query: {query}")
        print(f"Parameters: {params}")
        try:
            with SQLServerConnection() as conn:
                conn.raw_cursor.execute(query, params)
                rows = conn.raw_cursor.fetchall()
                columns = [column[0] for column in conn.raw_cursor.description]
                # Create XLSX in memory
                output = io.BytesIO()
                workbook = xlsxwriter.Workbook(output, {'in_memory': True})
                worksheet = workbook.add_worksheet('Report')
                # Write header
                for col_idx, col_name in enumerate(columns):
                    worksheet.write(0, col_idx, col_name)
                # Write data
                for row_idx, row in enumerate(rows, start=1):
                    for col_idx, value in enumerate(row):
                        if isinstance(value, bytes):
                            value = value.decode('utf-8', errors='replace')
                        worksheet.write(row_idx, col_idx, str(value))
                workbook.close()
                output.seek(0)
                return Response(
                    content=output.read(),
                    media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    headers={"Content-Disposition": "attachment; filename=work_order_report.xlsx"}
                )
        except Exception as e:
            logging.error(f"Database or XLSX error: {e}")
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
    raise HTTPException(status_code=404, detail="Report not found")
