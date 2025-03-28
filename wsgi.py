import atexit
from flask.cli import FlaskGroup
from src import app
from src.tasks.scheduler import schedule_tasks, scheduler

schedule_tasks()

atexit.register(lambda: scheduler.shutdown(wait=False))

cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
