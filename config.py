from dotenv import load_dotenv
import logging
import os
import pathlib
import json

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS_ID = list(map(int, os.getenv("ADMINS_ID").split(",")))
DEBUG = os.getenv("DEBUG")

BASE_DIR = pathlib.Path(__file__).parent
PAGES_DIR = BASE_DIR / "pages"
CURRENCY_FILE = BASE_DIR / "currency.json"

logger = logging.getLogger('bot')
logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)

logger_formatter = logging.Formatter('[%(asctime)s] %(name)s (%(levelname)s): %(message)s')
logger_handler = logging.StreamHandler()
logger_handler.setFormatter(logger_formatter)

logger.addHandler(logger_handler)

def get_curency():
    with open(CURRENCY_FILE, 'r') as f:
        return json.load(f)
    
def set_currency(new_data:dict):
    with open(CURRENCY_FILE, 'w') as f:
        json.dump(new_data, f)