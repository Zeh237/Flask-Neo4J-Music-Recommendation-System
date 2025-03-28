from apscheduler.schedulers.background import BackgroundScheduler
from src.services.DataIngestionService import Ingestion
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
ingestionService = Ingestion()
scheduler = BackgroundScheduler()

# Tasks
def setup_db_every_hour():
    response = ingestionService.load_all_to_neo4j()
    logging.info("neo4j database setup successful")
    return response

# scheduler
def schedule_tasks():
    scheduler.add_job(setup_db_every_hour, 'interval', hours=1, id='1')
    scheduler.start()
    logger.info("Task scheduling started.")
