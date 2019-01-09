import numpy as np
import pandas as pd
from datetime import datetime
from iexfinance.stocks import get_historical_intraday
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

##abc = "1997-06-30"
##abc = abc.mdates.strdate2num()
##print(abc)

print(datetime.now().date())
plt.style.use('ggplot')
df = pd.DataFrame()
df_date = pd.DataFrame()
df_open = pd.DataFrame()
df_high = pd.DataFrame()
df_low = pd.DataFrame()
df_close = pd.DataFrame()
date = datetime.today()
ohlc = pd.DataFrame()
ax = plt.subplot()

#df = get_historical_intraday("AAPL", output_format='pandas')
print(df.head())
##df = df[[ 'open', 'high', 'low', 'close']] 
##df = df.dropna(how='any')
##df = df.reset_index()
print(df.head())

##df_date = df[['minute']]
##df_open = df[['open']]
##df_high = df[['high']]
##df_low = df[['low']]
##df_close = df[['close']]

#data['Date2'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
#tuples = [tuple(x) for x in data[['Date2','Open','High','Low','Close']].values]

#df.to_csv('ohlc.csv')
df = pd.read_csv('ohlc.csv')
#df = df[[ 'minute', 'open', 'high', 'low', 'close']] 
print(df.head())


df['minute'] = str(datetime.now().date())+ str(' ') + df['minute'].astype(str)

#df['minute'] = pd.to_datetime(df['minute'])
#df['minute'] = df['minute'].map(mdates.date2num)
print(df.head())
##ax1 = datetime.strptime("2019-02-10 05:33", '%Y-%m-%d %H:%M')
##ax.xaxis.set_major_formatter(ax1)
df['minute'] = df['minute'].str.replace('-','')
df['minute'] = df['minute'].str.replace(' ','')
df['minute'] = df['minute'].str.replace(':','')
df['minute'] = df['minute'].astype(float)
#candlestick2_ohlc(ax, df_open, df_high, df_low, df_close)
print(df.head())
candlestick_ohlc(ax, df.values, colorup='g')
ax.plot()
plt.show()

