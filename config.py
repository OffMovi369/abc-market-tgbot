from dotenv import load_dotenv
import logging
import os

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS_ID = os.getenv("ADMINS_ID")
DEBUG = os.getenv("DEBUG")


logger = logging.getLogger('bot')
logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)

logger_formatter = logging.Formatter('[%(asctime)s] %(name)s (%(levelname)s): %(message)s')
logger_handler = logging.StreamHandler()
logger_handler.setFormatter(logger_formatter)

logger.addHandler(logger_handler)