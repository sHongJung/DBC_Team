import json
import pandas as pd
import numpy as np
import datetime
import time
import requests as rq
import matplotlib.pyplot as plt
from pprint import pprint

url = "https://min-api.cryptocompare.com/data/histoday"

parameters = {"fsym":"BTC","tsym":"USD","limit":"196"}

btc_json = rq.get(url, params=parameters).json()

btc_price=[]
btc_volume=[]
btc_timestamp=[]
btc_date=[]


# pprint(btc_json)

for data in btc_json['Data']:
    btc_price.append(data['close'])
    btc_volume.append(data['volumefrom'])
   #date = datetime.datetime.fromtimestamp(data['time']).isoformat()
    date = datetime.datetime.fromtimestamp(int(data['time'])).strftime('%Y-%m-%d')
    btc_date.append(date)
    btc_timestamp.append(data['time'])

x_axis = btc_date
y_axis = btc_price

print(btc_date)

df = pd.DataFrame({"Date":btc_date, "price":btc_price, "volume":btc_volume})
df.head()

# Export file as a CSV, without the Pandas index, but with the header
df.to_csv("Bitcoin_Price&Volume.csv", index=False, header=True)

plt.figure(figsize=(10,10))
plt.plot(x_axis, y_axis)
plt.xticks(np.arange(0,181,  step = 30), [btc_date[i] for i in np.arange(0,181,  step = 30)])
plt.show()