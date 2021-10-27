### Package Import ###
import os
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
### AppCode Import ###
from Server.Routes.UserRoutes import userRoute
from Server.Routes.BaseRoutes import baseRoute
from Server.Routes.TriggerRoutes import triggerRoute

###############################################################################

os.system("pyclean . -q")
program = FastAPI()
security = HTTPBearer()

###############################################################################

program.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

###############################################################################

program.include_router(userRoute)
program.include_router(baseRoute)
program.include_router(triggerRoute)


os.system("pyclean . -q")