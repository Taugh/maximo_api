# work_order_fields.py


# Updated list of work order fields for the Maximo API Project (from mapping template)
WORK_ORDER_FIELDS = [
    {"parameter_name": "work_order_num", "field_name": "wonum", "data_type": "string", "description": "work order number", "common": True, "required": False, "optional": False, "multi_entry": True, "notes": "Common"},
    {"parameter_name": "status", "field_name": "status", "data_type": "string", "description": "work order status", "common": True, "required": False, "optional": True, "multi_entry": False, "notes": "Required"},
    {"parameter_name": "statusdate", "field_name": "statusdate", "data_type": "datetime", "description": "date of status change", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": "Optional"},
    {"parameter_name": "work_order_type", "field_name": "worktype", "data_type": "string", "description": "WO type", "common": True, "required": False, "optional": True, "multi_entry": True, "notes": "Multi-Entry"},
    {"parameter_name": "description", "field_name": "description", "data_type": "string", "description": "WO description", "common": True, "required": False, "optional": True, "multi_entry": False, "notes": ""},
    {"parameter_name": "asset_number", "field_name": "assetnum", "data_type": "string", "description": "Asset number", "common": False, "required": False, "optional": True, "multi_entry": True, "notes": "Datetime (has upper/lower limit, both not required)"},
    {"parameter_name": "location", "field_name": "location", "data_type": "string", "description": "Location of tasks", "common": False, "required": False, "optional": True, "multi_entry": True, "notes": ""},
    {"parameter_name": "job_plan_num", "field_name": "jpnum", "data_type": "string", "description": "job plan", "common": False, "required": False, "optional": True, "multi_entry": True, "notes": ""},
    {"parameter_name": "changeby", "field_name": "changeby", "data_type": "string", "description": "Status/ownership changed by", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": ""},
    {"parameter_name": "changedate", "field_name": "changedate", "data_type": "datetime", "description": "datetime status/ownership changed", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": ""},
    {"parameter_name": "actlabhrs", "field_name": "actlabhrs", "data_type": "float", "description": "labor hours per associate", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": ""},
    {"parameter_name": "target_complete_date", "field_name": "targcompdate", "data_type": "datetime", "description": "target complete date", "common": True, "required": False, "optional": True, "multi_entry": False, "notes": "Common depending on work type"},
    {"parameter_name": "targstartdate", "field_name": "targstartdate", "data_type": "datetime", "description": "target start date", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": "Usually common for CMs"},
    {"parameter_name": "reported_by", "field_name": "reportedby", "data_type": "string", "description": "who reported the work order", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": "Optional for CM work types"},
    {"parameter_name": "report_date", "field_name": "reportdate", "data_type": "datetime", "description": "when the work order was reported", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": ""},
    {"parameter_name": "actstart", "field_name": "actstart", "data_type": "datetime", "description": "When the labor was started", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": ""},
    {"parameter_name": "actfinish", "field_name": "actfinish", "data_type": "datetime", "description": "when labor was finished", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": ""},
    {"parameter_name": "orgid", "field_name": "orgid", "data_type": "string", "description": "organization of work order", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": "Depending on if more than one org included"},
    {"parameter_name": "site_id", "field_name": "siteid", "data_type": "string", "description": "Site of work order", "common": True, "required": True, "optional": False, "multi_entry": True, "notes": ""},
    {"parameter_name": "istask", "field_name": "istask", "data_type": "int", "description": "is work order a task", "common": False, "required": True, "optional": False, "multi_entry": False, "notes": "Required for base query"},
    {"parameter_name": "woclass", "field_name": "woclass", "data_type": "string", "description": "is a work order or activity", "common": False, "required": True, "optional": False, "multi_entry": False, "notes": "Required for base query"},
    {"parameter_name": "owner", "field_name": "owner", "data_type": "string", "description": "owner of work order", "common": False, "required": False, "optional": True, "multi_entry": True, "notes": "Not all PMs are assigned an owner"},
    {"parameter_name": "owner_group", "field_name": "assignedownergroup", "data_type": "string", "description": "owner group of work order", "common": True, "required": False, "optional": True, "multi_entry": True, "notes": ""},
    {"parameter_name": "start_no_earlier", "field_name": "sneconstraint", "data_type": "datetime", "description": "earliest time a work order can be started", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": ""},
    {"parameter_name": "finish_no_later", "field_name": "fnlconstraint", "data_type": "datetime", "description": "lastest a work order can be completed before being flagged missed", "common": False, "required": False, "optional": True, "multi_entry": False, "notes": ""}
]
