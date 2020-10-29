import requests
import json
import config
from datetime import datetime
from win10toast import ToastNotifier
import time
import logging
import config

logging.basicConfig(
    level=logging.INFO,
    handlers=[ logging.FileHandler(config.LOG_PATH), logging.StreamHandler() ],
    format='%(asctime)s:%(levelname)s: %(message)s', 
)

def get_price():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

    querystring = {"region":config.STOCK_REGION,"symbol":config.STOCK_SYMBOL}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': config.API_KEY
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    p = response.json()["financialData"]["currentPrice"]["raw"]
    logging.info("Stock Price is {}".format(p))
    return p

def notify(price):
    toaster = ToastNotifier()
    toaster.show_toast("{} Stock Price Changed!".format(config.STOCK_SYMBOL),"THE PRICE IS {}".format(price),icon_path=config.ICON_PATH,duration=15)

price = get_price()
notify(price) 