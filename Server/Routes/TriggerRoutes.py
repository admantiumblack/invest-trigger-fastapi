### Package Import ###
from typing import Optional
from fastapi import APIRouter
from fastapi import Request, Body
### AppCode Import ###
from Server.Schema.TriggerSchema import TriggerSchemaDTO
import Server.Controller.TriggerController as tc

triggerRoute = APIRouter()
###############################################################################
@triggerRoute.get('/trigger', status_code=200)
def get_triggers(request:Request):
    res = tc.get_triggers(request)
    print(res)
    if type(res) == str:
        return {'message': res}
    else:
        return {'triggers': res}
################################################################################
@triggerRoute.post('/trigger/delete', status_code=200)
def delete_triggers(request: Request, signalId=Body(...)):
    res = tc.delete_triggers(request, signalId['signalId'])
    if type(res) == str:
        return {'message': res}
    else:
        return {'triggers': res}
##################################################################################
@triggerRoute.post('/trigger/insert', status_code=200)
def insert_triggers(request:Request, trigger:TriggerSchemaDTO):
    res = tc.insert_triggers(request, trigger)
    if type(res) == str:
        return {'message': res}
    else:
        return {'triggers': res}