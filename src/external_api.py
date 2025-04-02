import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

headers = {"apikey": api_key}


def get_amount_rub(transaction):
    amount = float(transaction.get("operationAmount").get("amount"))
    code = transaction.get("operationAmount").get("currency").get("code")

    if code in ["EUR", "USD"]:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={'RUB'}&from={code}&amount={amount}"
        response = requests.request("GET", url, headers=headers)
        return response.json().get("result")

    elif code == "RUB":
        return amount
