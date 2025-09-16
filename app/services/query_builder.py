# app/services/query_builder.py


def build_query(params):
    base_query = """
        SELECT wo.wonum, 
            wo.status, 
            wo.description, 
            a.assetnum, 
            a.description AS asset_desc
        FROM workorder wo
            LEFT JOIN asset as a 
        ON wo.assetnum = a.assetnum
    """
    where_clauses = []
    values = []

    # Fixed values for woclass
    where_clauses.append("wo.woclass IN (?, ?)")
    values.extend(['WORKORDER', 'ACTIVITY'])

    # Default value for orgid
    orgid = params.get('orgid', 'US')
    where_clauses.append("wo.orgid = ?")
    values.append(orgid)

    # Default value for siteid
    siteid = params.get('siteid', 'FWN')
    where_clauses.append("wo.siteid = ?")
    values.append(siteid)

    # Default value for historyflag
    history = params.get('history', 0)
    if history is None:
        where_clauses.append("wo.historyflag IS NULL")
    else:
        where_clauses.append("wo.historyflag = ?")
        values.append(history)

    # User-supplied filters

    if 'work_order_num' in params and params['work_order_num']:
        where_clauses.append("wo.wonum = ?")
        values.append(params['work_order_num'])
    if 'status' in params and params['status']:
        where_clauses.append("wo.status = ?")
        values.append(params['status'])
    if 'worktype' in params and params['worktype']:
        where_clauses.append("wo.worktype = ?")
        values.append(params['worktype'])
    if 'assignedownergroup' in params and params['assignedownergroup']:
        where_clauses.append("wo.assignedownergroup = ?")
        values.append(params['assignedownergroup'])
    if 'asset_number' in params and params['asset_number']:
        where_clauses.append("asset.assetnum = ?")
        values.append(params['asset_number'])
    # Add more fields as needed...

    if where_clauses:
        base_query += " WHERE " + " AND ".join(where_clauses)

    return base_query, tuple(values)
