### Package Import ###
from fastapi import APIRouter
from Server.ScheduledJobs.Trigger import check_trigger
### AppCode Import ###
baseRoute = APIRouter()
###############################################################################
@baseRoute.get('/', status_code=201)
def hello_world():
    # check_trigger('30m')
    return {'message':'hello world'}