import atexit
from flask.cli import FlaskGroup

from src import app

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from src.jobs.background_jobs import *

scheduler = BackgroundScheduler()
# trigger = CronTrigger(year="*", month="*", day="*", hour="*", minute="*", second="*")
# scheduler.add_job(lambda: retrain_models(app), trigger="interval", days=3)
trigger_1 = CronTrigger(year="*", month="*", day="*/2", hour="0", minute="0", second="0")
trigger_2 = CronTrigger(year="*", month="*", day="*/2", hour="1", minute="0", second="0")
trigger_3 = CronTrigger(year="*", month="*", day="*/2", hour="2", minute="0", second="0")
trigger_4 = CronTrigger(year="*", month="*", day="*/2", hour="3", minute="0", second="0")
trigger_5 = CronTrigger(year="*", month="*", day="*/2", hour="4", minute="0", second="0")
# scheduler.add_job(lambda: print_name(app, "harvey"), trigger=trigger)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()
