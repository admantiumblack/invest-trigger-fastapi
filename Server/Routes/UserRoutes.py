### Package Import ###
from fastapi import APIRouter
from fastapi import Response, Request
### AppCode Import ###
from Server.Controller.UserController import *
from Server.Schema.UserSchema import UserSchemaDTO
userRoute = APIRouter()
###############################################################################
@userRoute.post('/user/login', status_code=201)
def login(response:Response, request:Request, user:UserSchemaDTO):
    message = user_login(response, request, user)
    return {'message':message}
###############################################################################
@userRoute.post('/user/register', status_code=201)
def register(request:Request, user:UserSchemaDTO):
    message = register_user(request, user)
    return {'message':message}
###############################################################################
@userRoute.post('/user/edit-profile', status_code=201)
def edit_profile(request:Request, user: UserSchemaDTO):
    message = update_profile(request, user)
    return {'message':message}
###############################################################################
@userRoute.post('/user/logout', status_code=201)
def logout(response:Response):
    message = user_logout(response)
    return {'message':message}