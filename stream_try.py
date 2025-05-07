import pandas as pd
import requests
import time
from datetime import datetime
from sqlalchemy import create_engine
import psycopg2

con=psycopg2.connect(
#psql bağlanama
host="localhost",
port=5432,
database="crypto_prices",
user="postgres",
password="4516"
)

cc=con.cursor()

# sqlalchemy bağlantı mororu
engine=create_engine("postgresql://postgres:4516@localhost:5432/crypto_prices")



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
      url=f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={idy}&price_change_percentage=7d,30d,1y"
      data=requests.get(url).json()
 
      for coin in data: 
              
             symbol=coin.get("id") #adı
             price=coin.get("current_price") #fiyatı
             hours_24_change=coin.get("price_change_percentage_24h") #24 saatlik fiytat değişimi
             high=coin.get("high_24h") #24 saatdeki en yüksek fiyat
             low=coin.get("low_24h")#24 saatdeki en düşük fiyat
             volume=coin.get("total_volume")# 24 saatdeki işlem saati
             market_cap=coin.get("market_cap")#piyasa değeri
             price_change_1y=coin.get("price_change_percentage_1y_in_currency")
             price_change_30d=coin.get("price_change_percentage_30d_in_currency")
             price_change_7d=coin.get("price_change_percentage_7d_in_currency")

           
            
                 
             print(f"[{datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}] {symbol.capitalize()}: ${price:.2f},${price_change_1y:.2f},${price_change_30d:.2f},${price_change_7d:.2f} , 24 Saatlik Değişim: {hours_24_change}%, En Yüksek: {high}, En Düşük: {low}, Hacim: {volume}, Piyasa Değeri: {market_cap} ")
            
             prices.append([datetime.now(), symbol,  price, price_change_1y, price_change_30d, price_change_7d, hours_24_change, high, low, price_change_1y,volume, market_cap])   
            
     
            
      df=pd.DataFrame(prices, columns=["Date", "Coin", "Price","price_change_1y","price_change_30d","price_change_7d", "hours_24_change", "high", "low","price_change_1y" , "volume", "market_cap"])
      
     

      if df.isnull().sum().sum()==0:
           
           print("eksik veri var ") 
      else:
          df.dropna(inplace=True)
     
      
          
     
      print(df.info())
      print(df.describe())
    

      df.to_csv("crypto_prc.csv", mode='w' ,header=True , index=False  )
      
      # dataframe yi postgresql e aktar 
      df.to_sql("crypto_prices", engine, if_exists="append", index=False)

             

      time.sleep(60)


     except Exception as e:                                                                                                                                                                  
      print("tekrar deneyiniz : " , e)
      time.sleep(60)