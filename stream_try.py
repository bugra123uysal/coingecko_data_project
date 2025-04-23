import pandas as pd
import requests
import time
from datetime import datetime

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
      url=f"https://api.coingecko.com/api/v3/simple/price?ids={idy}&vs_currencies=usd"
      data=requests.get(url).json()
      for symbol in stock:     
            if symbol in data:                                                                                                                                                                                 
                 price=data[symbol]['usd']
                 print(f"[{datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}] {symbol.capitalize()}: ${price:.2f}")
                 prices.append([datetime.now(), symbol, price ])    
     
            else:
                print("sorun oluştu sorun için şimdiden özür dileriz")       
      df=pd.DataFrame(prices, columns=["Data", "Price", "Coin"])
      df.to_csv("crypto_prc.csv", mode='w' ,header=True , index=False  )


      time.sleep(60)


     except Exception as e:                                                                                                                                                                  
      print("tekrar deneyiniz : " , e)
      time.sleep(60)
