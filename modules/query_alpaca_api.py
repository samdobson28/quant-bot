# query_alpaca_api.py

import requests
import os

# Set the Alpaca.Markets API Key
API_KEY = os.getenv('ALPACA_API')
API_SECRET = os.getenv('ALPACA_SECRET_API')

def query_alpaca_api_v1beta3(url: str, params: dict) -> dict:
    """
    Base function for querying the Alpaca.Markets API (v1beta3).
    """
    headers = {
        'accept': 'application/json',
        'APCA-API-KEY-ID': API_KEY,
        'APCA-API-SECRET-KEY': API_SECRET,
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Alpaca API: {e}")
        raise
