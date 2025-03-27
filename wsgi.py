import atexit
from flask.cli import FlaskGroup
from src import app
from apscheduler.schedulers.background import BackgroundScheduler


cli = FlaskGroup(app)

if __name__ == "__main__":
    cli()
