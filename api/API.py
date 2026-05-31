from dotenv import load_dotenv
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

headers = {
    "X-API-Key": API_KEY
}

url = "https://api.datasectors.com/api/chart/price"


params = {
    "symbol": "IDX:BBCA",
    "interval": "1d",
    "from": "2026-05-25",
    "to": "2026-05-31",
    "limit": 1000
}

response = requests.get(url, headers=headers, params=params)

data = response.json()
print(json.dumps(data, indent=2))

