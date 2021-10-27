### Package Import ###
from fastapi import APIRouter
from fastapi import Response, Request
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