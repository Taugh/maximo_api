# work_order_fields.py

# List of work order fields for the Maximo API Project (first stage)
# Each field is represented as a dictionary with relevant metadata

WORK_ORDER_FIELDS = [
    {
        "parameter_name": "work_order_num",
        "field_name": "wonum",
        "data_type": "string",
        "description": "work order number",
        "common": True,
        "required": False,
        "optional": False,
        "multi_entry": True,
        "notes": "Common"
    },
    {
        "parameter_name": "status",
        "field_name": "status",
        "data_type": "string",
        "description": "work order status",
        "common": True,
        "required": False,
        "optional": True,
        "multi_entry": False,
        "notes": "Required"
    },
    {
        "parameter_name": "statusdate",
        "field_name": "statusdate",
        "data_type": "datetime",
        "description": "date of status change",
        "common": False,
        "required": False,
        "optional": True,
        "multi_entry": False,
        "notes": "Optional"
    },
    {
        "parameter_name": "work_order_type",
        "field_name": "worktype",
        "data_type": "string",
        "description": "WO type",
        "common": True,
        "required": False,
        "optional": True,
        "multi_entry": True,
        "notes": "Multi-Entry"
    },
    {
        "parameter_name": "description",
        "field_name": "description",
        "data_type": "string",
        "description": "WO description",
        "common": True,
        "required": False,
        "optional": True,
        "multi_entry": False,
        "notes": ""
    },
    {
        "parameter_name": "asset_number",
        "field_name": "assetnum",
        "data_type": "string",
        "description": "Asset number",
        "common": False,
        "required": False,
        "optional": True,
        "multi_entry": True,
        "notes": "Datetime (has upper/lower limit, both not required)"
    },
    {
        "parameter_name": "location",
        "field_name": "location",
        "data_type": "string",
        "description": "Location of tasks",
        "common": False,
        "required": False,
        "optional": True,
        "multi_entry": True,
        "notes": ""
    },
    {
        "parameter_name": "job_plan_num",
        "field_name": "jpnum",
        "data_type": "string",
        "description": "job plan",
        "common": False,
        "required": False,
        "optional": True,
        "multi_entry": True,
        "notes": ""
    },
    # ... (add the rest of the fields as needed, following the same structure)
]
