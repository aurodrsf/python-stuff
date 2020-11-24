# criação de um simples programa para puxar preços de ações e criar plots

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015,1,1) # data de ínicio e fim da consulta, além de perguntar 
end = dt.datetime.now()
ticker = input("Digite um ticker para consultar seu preço:")

df = web.DataReader(ticker, "yahoo", start, end) # cria um data frame com os dados OHLC 

df.to_csv('ticker.csv') # Cria um arquivo CSV com os dados do ticker

df = pd.read_csv('ticker.csv', parse_dates = True, index_col=0) # Plota a série temporal do preço high do ticker
df.plot()
plt.show()

df['Adj Close'].plot()
plt.show()

df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
print(df.tail())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()




