### Package Import ###
from fastapi import APIRouter, Body
from fastapi.param_functions import Depends
from starlette.routing import Route
### AppCode Import ###
from Server.Controller.ControllerModel1 import Model1Predict
from Server.Model.BaseModel import BaseModelDTO

BaseRoute = APIRouter()

###############################################################################

@BaseRoute.get('/', description="API Entry")
async def Info():
    return "Hello World"

@BaseRoute.post('/trigger/api1', description="API 1")
async def Func1(parameter:BaseModelDTO=Body(...)): ## ngebaca parameter dari body
    insert_result = await Model1Predict(parameter)
    return insert_result

@BaseRoute.get('/trigger/api2', description="API 2")
async def Func2():
    return "Hello API2"

@BaseRoute.get('/trigger/api3', description="API 3")
async def Func3():
    return "Hello API3"

@BaseRoute.get('/trigger/api4', description="API 4")
async def Func4():
    return "Hello API4"

###############################################################################