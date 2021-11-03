from apscheduler.schedulers.background import BackgroundScheduler
from Server.ScheduledJobs.Trigger import check_trigger
import pytz
# '30m', '1h', '2h', '4h', '6h', '8h', '12h'
scheduler = BackgroundScheduler(timezone=pytz.timezone('asia/jakarta'))
def start_triggers():
    scheduler.remove_job('startup')
    scheduler.add_job(check_trigger, 'interval', minutes=30, kwargs={'timeframe':'30m'})
    scheduler.add_job(check_trigger, 'interval', hours=1, kwargs={'timeframe':'1h'})
    scheduler.add_job(check_trigger, 'interval', hours=2, kwargs={'timeframe':'1h'})
    scheduler.add_job(check_trigger, 'interval', hours=4, kwargs={'timeframe':'1h'})
    scheduler.add_job(check_trigger, 'interval', hours=6, kwargs={'timeframe':'1h'})
    scheduler.add_job(check_trigger, 'interval', hours=8, kwargs={'timeframe':'1h'})
    scheduler.add_job(check_trigger, 'interval', hours=12, kwargs={'timeframe':'1h'})

