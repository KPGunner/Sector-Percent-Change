import pandas as pd
import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt
import csv

###Since Yahoo pulled their API the DataReader will not longer work. Can still work with a .csv###

#GFC#
##start = dt.datetime(2007, 10, 9)
##end = dt.datetime(2009, 3, 9)

###Custom#
start = dt.datetime(2015, 1, 1)
end = dt.datetime(2018, 3, 21)


#Sector Tickers#
#tickers = ['XLV', 'XLU', 'XLE', 'XLB', 'XLI', 'XLP', 'XLRE', 'XLF', 'XLY', 'XLK', 'AGG', 'SPY']

#Defense Tickers#
#tickers = ['BA', 'UTX', 'LMT', 'GD', 'RTN', 'COL', 'LLL', 'TDG', 'HII', 'SPR', 'XAR', 'ITA', 'SPY', 'NOC']

tickers = ['SPYB', 'SYLD', 'IPKW', 'FYLD', 'SPY']

df = web.DataReader(tickers, 'yahoo', start, end)

price = df['Adj Close']
#price= df['Close']

#Manipulate data to pull change from start to end#
df1 = price.iloc[[0, -1]]
print(df1)

pct = df1.pct_change()*100

print(pct)
#pct.to_csv('da.csv')

df2 = df1.iloc[[0, -1]] = df1.iloc[[-1, 0]]
print(df2)
change = df2.pct_change()*100

print(change)
#change.to_csv('Pct.csv')


#Pull and plot just daily percent change#

##df3 = price.pct_change()

##df3.plot()
##plt.title('Daily Sector Percent Change')
##plt.show()


#change.to_csv('Defense.csv')




