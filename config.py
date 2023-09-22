from dotenv import load_dotenv
import logging
import os
import pathlib

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS_ID = os.getenv("ADMINS_ID")
print(type(ADMINS_ID))
DEBUG = os.getenv("DEBUG")

BASE_DIR = pathlib.Path(__file__).parent
PAGES_DIR = BASE_DIR / "pages"

logger = logging.getLogger('bot')
logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)

logger_formatter = logging.Formatter('[%(asctime)s] %(name)s (%(levelname)s): %(message)s')
logger_handler = logging.StreamHandler()
logger_handler.setFormatter(logger_formatter)

logger.addHandler(logger_handler)