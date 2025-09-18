# app/services/query_builder.py



def build_query(params, select_fields=None):
    # Use provided select_fields or default to all mapped fields
    if select_fields is None:
        select_fields = [
            "wo.wonum", "wo.status", "wo.statusdate", "wo.description", "wo.siteid", "wo.worktype", "wo.assignedownergroup",
            "wo.changeby", "wo.changedate", "wo.actlabhrs", "wo.targcompdate", "wo.targstartdate", "wo.reportedby", "wo.reportdate",
            "wo.actstart", "wo.actfinish", "wo.orgid", "wo.istask", "wo.woclass", "wo.owner", "wo.sneconstraint", "wo.fnlconstraint",
            "a.assetnum", "a.description AS assetdesc", "wo.location", "wo.jpnum"
        ]
    base_query = f"SELECT {', '.join(select_fields)} FROM workorder wo LEFT JOIN asset as a ON wo.assetnum = a.assetnum and wo.siteid = a.siteid"
    where_clauses = []
    values = []

    # Required/fixed values
    woclass = params.get('woclass', 'WORKORDER')
    if isinstance(woclass, list):
        where_clauses.append(f"wo.woclass IN ({', '.join(['?' for _ in woclass])})")
        values.extend(woclass)
    else:
        where_clauses.append("wo.woclass = ?")
        values.append(woclass)

    orgid = params.get('orgid', 'US')
    where_clauses.append("wo.orgid = ?")
    values.append(orgid)

    siteid = params.get('site_id', ['FWN'])
    if isinstance(siteid, list):
        where_clauses.append(f"wo.siteid IN ({', '.join(['?' for _ in siteid])})")
        values.extend(siteid)
    else:
        where_clauses.append("wo.siteid = ?")
        values.append(siteid)

    history = params.get('historyflag', 0)
    if history is None:
        where_clauses.append("wo.historyflag IS NULL")
    else:
        where_clauses.append("wo.historyflag = ?")
        values.append(history)

    # User-supplied filters for all mapped fields
    field_map = {
        "work_order_num": "wo.wonum",
        "status": "wo.status",
        "statusdate": "wo.statusdate",
        "worktype": "wo.worktype",
        "description": "wo.description",
        "asset_number": "a.assetnum",
        "location": "wo.location",
        "job_plan_num": "wo.jpnum",
        "changeby": "wo.changeby",
        "changedate": "wo.changedate",
        "actlabhrs": "wo.actlabhrs",
        "target_complete_date": "wo.targcompdate",
        "targstartdate": "wo.targstartdate",
        "reported_by": "wo.reportedby",
        "report_date": "wo.reportdate",
        "actstart": "wo.actstart",
        "actfinish": "wo.actfinish",
        "owner": "wo.owner",
        "owner_group": "wo.assignedownergroup",
        "start_no_earlier": "wo.sneconstraint",
        "finish_no_later": "wo.fnlconstraint"
    }
    for param, db_field in field_map.items():
        value = params.get(param)
        if value:
            if isinstance(value, list):
                where_clauses.append(f"{db_field} IN ({', '.join(['?' for _ in value])})")
                values.extend(value)
            else:
                where_clauses.append(f"{db_field} = ?")
                values.append(value)

    if where_clauses:
        base_query += " WHERE " + " AND ".join(where_clauses)

    return base_query, tuple(values)
