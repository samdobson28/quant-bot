# settings.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

PAPER_TRADING = True
API_KEY = os.getenv("ALPACA_API_KEY")
API_SECRET = os.getenv("ALPACA_API_SECRET")
ALPACA_BASE_URL = os.getenv("ALPACA_BASE_URL")
