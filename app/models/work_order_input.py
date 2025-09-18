# Pydantic models for work order input

from pydantic import BaseModel
from enum import Enum
from typing import Optional, List


class WOStatus(str, Enum):
    APPR = 'APPR'
    CAN = 'CAN'
    CLOSE = 'CLOSE'
    COMP = 'COMP'
    CORRECTED = 'CORRECTED'
    CORRTD = 'CORRTD'
    FLAGGED = 'FLAGGED'
    MISSED = 'MISSED'
    PENDPROD = 'PENDPROD'
    PENDQA = 'PENDQA'
    PENRVW = 'PENRVW'
    REVWD = 'REVWD'
    INPRG = 'INPRG'
    WAPPR = 'WAPPR'



# Enum for allowable work order types
class WOWorkType(str, Enum):
    CA = 'CA'
    CAL = 'CAL'
    CM = 'CM'
    CO = 'CO'
    DOCRV = 'DOCRV'
    ECO = 'ECO'
    NMC = 'NMC'
    PM = 'PM'
    RM = 'RM'
    RQL = 'RQL'
    SAMPM = 'SAMPM'
    SMD = 'SMD'
    VAL = 'VAL'
    
    
# Enum for allowable owner groups
class AssignedOwnerGroup(str, Enum):
    FWNAE = 'FWNAE'
    FWNAST = 'FWNAST'
    FWNAST1 = 'FWNAST1'
    FWNCAD = 'FWNCAD'
    FWNCCM = 'FWNCCM'
    FWNCI = 'FWNCI'
    FWNCS = 'FWNCS'
    FWNCSM = 'FWNCSM'
    FWNCSR = 'FWNCSR'
    FWNCSS = 'FWNCSS'
    FWNDCQ = 'FWNDCQ'
    FWNEN2 = 'FWNEN2'
    FWNFMOP = 'FWNFMOP'
    FWNHR = 'FWNHR'
    FWNHSE = 'FWNHSE'
    FWNITOP = 'FWNITOP'
    FWNLC1 = 'FWNLC1'
    FWNLCP1 = 'FWNLCP1'
    FWNLCP2 = 'FWNLCP2'
    FWNLCP3 = 'FWNLCP3'
    FWNLCP4 = 'FWNLCP4'
    FWNMC1 = 'FWNMC1'
    FWNMCS = 'FWNMCS'
    FWNMDC = 'FWNMDC'
    FWNMET = 'FWNMET'
    FWNMICR1 = 'FWNMICR1'
    FWNMICR2 = 'FWNMICR2'
    FWNMNTSCH = 'FWNMNTSCH'
    FWNMOS = 'FWNMOS'
    FWNPA1 = 'FWNPA1'
    FWNPE = 'FWNPE'
    FWNPS = 'FWNPS'
    FWNPSC = 'FWNPSC'
    FWNPSM = 'FWNPSM'
    FWNPSP = 'FWNPSP'
    FWNPSP1 = 'FWNPSP1'
    FWNPSP2 = 'FWNPSP2'
    FWNPSP3 = 'FWNPSP3'
    FWNPSP4 = 'FWNPSP4'
    FWNPSP5 = 'FWNPSP5'
    FWNPSP6 = 'FWNPSP6'
    FWNPSP7 = 'FWNPSP7'
    FWNQACA = 'FWNQACA'
    FWNQACL = 'FWNQACL'
    FWNQACP = 'FWNQACP'
    FWNQALO = 'FWNQALO'
    FWNQAMI = 'FWNQAMI'
    FWNQAOP = 'FWNQAOP'
    FWNQAOP1 = 'FWNQAOP1'
    FWNQAW = 'FWNQAW'
    FWNQCAST = 'FWNQCAST'
    FWNQOI = 'FWNQOI'
    FWNRECMGT = 'FWNRECMGT'
    FWNRXM = 'FWNRXM'
    FWNSQA = 'FWNSQA'
    FWNVAL = 'FWNVAL'
    FWNWSM = 'FWNWSM'


class WorkOrderInput(BaseModel):
    work_order_num: Optional[List[str]] = None
    status: Optional[WOStatus] = None
    statusdate: Optional[str] = None
    work_order_type: Optional[WOWorkType] = None
    description: Optional[str] = None
    asset_number: Optional[List[str]] = None
    location: Optional[List[str]] = None
    job_plan_num: Optional[List[str]] = None
    changeby: Optional[str] = None
    changedate: Optional[str] = None
    actlabhrs: Optional[float] = None
    target_complete_date: Optional[str] = None
    targstartdate: Optional[str] = None
    reported_by: Optional[str] = None
    report_date: Optional[str] = None
    actstart: Optional[str] = None
    actfinish: Optional[str] = None
    orgid: Optional[str] = None
    site_id: Optional[List[str]] = None
    istask: Optional[int] = None
    woclass: Optional[str] = None
    owner: Optional[List[str]] = None
    owner_group: Optional[List[str]] = None
    start_no_earlier: Optional[str] = None
    finish_no_later: Optional[str] = None
    assignedownergroup: Optional[AssignedOwnerGroup] = None
    worktype: Optional[WOWorkType] = None
