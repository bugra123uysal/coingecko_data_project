import pandas as pd
import requests
import time
from datetime import datetime

stock = ["bitcoin", "ethereum", "solana", "tether", "binancecoin"]
while True:
     prices=[]
     for symbol in stock:
         url=f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
         aa =requests.get(url).json()
         price=aa[symbol]['usd']
         print(f"[{datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}] {symbol.capitalize()}: ${price:.2f}")
         prices.append([datetime.now(), symbol, price ])
    
     df=pd.DataFrame(prices, columns=["Data", "Price", "Coin"])
     df.to_csv("crypto_prc.csv", mode='w' ,header=True , index=False  )



     time.sleep(60)




