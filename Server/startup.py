### Package Import ###
import os
from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
# from apscheduler.schedulers.background import BackgroundScheduler
### AppCode Import ###
from Server.Routes.UserRoutes import userRoute
from Server.Routes.BaseRoutes import baseRoute
from Server.Routes.TriggerRoutes import triggerRoute
from Server.ScheduledJobs.Scheduler import scheduler, start_triggers

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

# scheduler = BackgroundScheduler()

@program.on_event('startup')
def on_startup():
    scheduler.add_job(start_triggers, 'cron', hour='0', id='startup')
    scheduler.start()

@program.on_event('shutdown')
def on_shutdown():
    scheduler.shutdown(wait=False)