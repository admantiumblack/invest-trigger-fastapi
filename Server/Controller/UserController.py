### Package Import ###
from fastapi import Response, Request
from datetime import timedelta
### AppCode Import ###
from Server.Schema.UserSchema import UserSchemaDTO, UserRegisterSchemaDTO
from Server.Model import UserModel as um


def user_login(response:Response, request:Request, user:UserSchemaDTO):
    try:
        if request.cookies.get("Authorization") is not None:
            return 'login failed, already logedin'
    except:
        pass
    userResult = um.user_login(user)
    if len(userResult) == 1:
        userId = userResult[0][0]
        response.set_cookie('Authorization', str(userId), expires=timedelta(days=1))
        return 'login success'
    else:
        return 'login failed'

###############################################################################
def check_username(username: str):
    userResult = um.get_username(username)

    return len(userResult) == 0
###############################################################################
def check_email(email: str):
    userResult = um.get_email(email)

    return len(userResult) == 0
###############################################################################
def register_user(request:Request, user:UserRegisterSchemaDTO):
    try:
        if request.cookies.get("Authorization") is not None:
            return 'user loggedin'
    except:
        pass

    validUsername = check_username(user.username)
    validEmail = check_email(user.email)

    if validUsername and validEmail:
        try:
            userDict = {
                'Username' : user.username,
                'Email': user.email,
                'Password': user.password,
                'FullName': user.fullName
            }
            userDict = {k: v for k, v in userDict.items() if v is not None}
            print(userDict)
            um.register_user(userDict)
            return 'success'
        except:
            return 'register failed'
    elif not validUsername:
        return 'username not available'
    elif not validEmail:
        return 'email not available'

###############################################################################
def update_profile(request:Request, user: UserSchemaDTO):

    userProfileDict = {}

    if user.username is not None:
        validusername = check_username(user.username)
        if validusername:
            userProfileDict['Email'] = user.username
        else:
            return 'username invalid'

    if user.fullName is not None:
        userProfileDict['FullName'] = user.fullName

    if user.password is not None:
        userProfileDict['Password'] = user.password

    try:
        um.update_profile(request.cookies.get("Authorization"), userProfileDict)
        return 'update success'
    except:
        return 'user not authorized'
###############################################################################
def user_logout(response:Response):
    try:
        response.delete_cookie('Authorization')
    except:
        return 'logout failed'
    return 'logout success'
###############################################################################
def get_user_profile(request:Request):
    try:
        res = um.get_user_profile(request.cookies.get('Authorization'))
        if len(res) != 1:
            return 'retrieval failed'
        return res[0]
    except Exception as e:
        return 'user not available'