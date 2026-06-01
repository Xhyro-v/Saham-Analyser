from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()

API_KEY = os.getenv("API_KEY")

BASE_URL = "https://api.datasectors.com/api/chart/price"

headers = {
    "X-API-Key": API_KEY
}


def get_stock_data(symbol, start_date, end_date, limit=500):
    params = {
        "symbol": symbol,
        "interval": "1d",
        "limit": limit
    }

    response = requests.get(BASE_URL, headers=headers, params=params)
    data = response.json()

    if not data.get("data"):
        print("No data received")
        return []
  
    filtered = []
    for d in data["data"]:
        date = d["datetime"][:10]
        if start_date <= date <= end_date:
            filtered.append(d)

    return filtered