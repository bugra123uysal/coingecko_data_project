import pandas as pd
import yfinance as yf
import time
from datetime import datetime

stock=["AAPL","TSLA","MSFT" ]

while True:
    for symbol in stock:

     aa=yf.Ticker(symbol)
     bb=aa.history(period="1d", interval="1m")
     
      
      #en son satırır alır
     last_row=bb.tail(1)
     if not last_row.empty: 

        print(f"[{datetime.now().strftime('%y-%m-%d %H:%M:%S')}] {symbol} Fiyat: {last_row['Close'].values[0]:.2f}USD")
       
     else:
       print("tekrar deneyiniz")
    time.sleep(60)