import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

aa=pd.read_csv("C:\\Users\\buğra\\Desktop\\stream_stock\\crypto_prc.csv")

print(aa.columns)

""" 
sns.barplot(y="Price",x="Coin",data=aa)
plt.title("coin prices")
plt.show()



sns.barplot(x="Coin", y="price_change_1y", data=aa)
plt.title("1 year")
plt.show()

sns.barplot(x="Coin", y="price_change_30d" ,data=aa)
plt.title("30 days")
plt.show()

sns.barplot(x="Coin", y="price_change_7d" ,data=aa)
plt.title("7 days")
plt.show()
 """
sns.scatterplot(x="Coin",y="volume", data=aa)
plt.title("coin volume")
plt.show()

sns.scatterplot(x="Coin", y="market_cap", data=aa)
plt.title("coin market cap")
plt.show()


