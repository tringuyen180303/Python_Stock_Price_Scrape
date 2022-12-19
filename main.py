import json

import requests
from bs4 import BeautifulSoup

def getprice(symbol):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                             "AppleWebKit/537.36 (KHTML, like Gecko)"
                             " Chrome/108.0.0.0 Safari/537.36"}
    url =f"https://finance.yahoo.com/quote/{symbol}?p={symbol}&.tsrc=fin-srch"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    stock = {
        "symbol": symbol,
        "price" : soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all("fin-streamer")[0]["value"],
        "percent_change" : soup.find('div', {'class': "D(ib) Mend(20px)"}).find_all("fin-streamer")[2]["value"]}
    return stock
final_data = []
stocks = ["AAPL", "MSFT", "GOOGL", "NVDA"]
for s in stocks:
    new = getprice(s)
    print(new)
    final_data.append(new)

with open("stockdata.json", "w") as f:
    json.dump(final_data, f)


