### Package Import ###
from fastapi import APIRouter
### AppCode Import ###
baseRoute = APIRouter()
###############################################################################
@baseRoute.get('/', status_code=201)
def hello_world():
    return {'message':'hello world'}