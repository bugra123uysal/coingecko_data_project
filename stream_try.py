import pandas as pd
import requests
import time
from datetime import datetime
import psycopg2




stock = [ "bitcoin", "ethereum", "tether", "binancecoin", "solana",
    "ripple", "usd-coin", "cardano", "avalanche-2", "dogecoin",
    "toncoin", "polkadot", "chainlink", "polygon", "wrapped-bitcoin",
    "shiba-inu", "tron", "uniswap", "litecoin", "internet-computer",
    "dai", "bitcoin-cash", "ethereum-classic", "cosmos", "stellar",
    "okb", "monero", "lido-dao", "aptos", "filecoin",
    "hedera", "arbitrum", "crypto-com-chain", "vechain", "near",
    "immutable-x", "optimism", "quant-network", "the-graph", "algorand",
    "render-token", "aave", "flow", "elrond-erd-2", "stacks",
    "the-sandbox", "axie-infinity", "tezos", "theta-token", "decentraland"]
while True:
     try:
      
      prices=[]
      idy=",".join(stock) 
      url=f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={idy}"
      data=requests.get(url).json()
      for coin in data: 
              
             symbol=coin.get("id") #adı
             price=coin.get("current_price") #fiyatı
             hours_24_change=coin.get("price_change_percentage_24h") #24 saatlik fiytat değişimi
             high=coin.get("high_24h") #24 saatdeki en yüksek fiyat
             low=coin.get("low_24h")#24 saatdeki en düşük fiyat
             volume=coin.get("total_volume")# 24 saatdeki işlem saati
             market_cap=coin.get("market_cap")#piyasa değeri

            
                 
             print(f"[{datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}] {symbol.capitalize()}: ${price:.2f} 24 Saatlik Değişim: {hours_24_change}%, En Yüksek: {high}, En Düşük: {low}, Hacim: {volume}, Piyasa Değeri: {market_cap} ")
             prices.append([datetime.now(), symbol, price,hours_24_change,high, low, volume ,market_cap ])    
     
                 
      df=pd.DataFrame(prices, columns=["Data", "Price", "Coin","hours_24_change","high", "low","volum","market_cap"])
      df.to_csv("crypto_prc.csv", mode='w' ,header=True , index=False  )


      time.sleep(60)


     except Exception as e:                                                                                                                                                                  
      print("tekrar deneyiniz : " , e)
      time.sleep(60)