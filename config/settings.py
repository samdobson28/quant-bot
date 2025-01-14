# settings.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PAPER_TRADING = True
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL")