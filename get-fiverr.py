import requests
import json
import config
from datetime import datetime
from win10toast import ToastNotifier
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[ logging.FileHandler(r"D:\DevOps\python\rapidAPI\yahoo-finance-api\prices.log"), logging.StreamHandler() ],
    format='%(asctime)s:%(levelname)s: %(message)s', 
)

def get_price():
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/get-detail"

    querystring = {"region":"US","symbol":"FVRR"}

    headers = {
        'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
        'x-rapidapi-key': "eb185261abmshce945baa82d97a1p16fe8cjsn9e7fe2f909d2"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    p = response.json()["financialData"]["currentPrice"]["raw"]
    logging.info("Stock Price is {}".format(p))
    return p

def notify(price):
    toaster = ToastNotifier()
    toaster.show_toast("FVRR Stock Price Changed!","THE PRICE IS {}".format(price),icon_path=r"D:\DevOps\python\rapidAPI\yahoo-finance-api\bull.ico",duration=15)

price = get_price()
notify(price)
while True:
    new_price = get_price()
    if new_price != price and price is not None:
        notify(new_price)
        price = new_price
    time.sleep(60)