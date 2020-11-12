import numpy as np
import pandas as pd
from datetime import datetime
from iexfinance.stocks import get_historical_intraday
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import matplotlib.ticker as mtick

def chart(ticker):

    plt.style.use('ggplot')
    df = pd.DataFrame()
    ax = plt.subplot()

    print(datetime.now().date())
    df = get_historical_intraday(ticker, output_format='pandas', token="<pk_a969baae0f744abd905865e2d5d0acfa>")
    print(df.head())

    df = df[['average']] 
    df = df.dropna(how='any')
    print(df.head())
    df = df.reset_index()
    print(df.head())

    df.to_csv('avgprice.csv')

    df['minute'] = str(datetime.now().date())+ str(' ') + df['minute'].astype(str)
    print(df.head())

    df['minute'] = pd.to_datetime(df['minute'])
    df['minute'] = df['minute'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
    minlocator = mdates.MinuteLocator(byminute=[0,30]) 
    ax.xaxis.set_major_locator(minlocator)
    print(df.head())

    plt.title(ticker + '  ' + str(datetime.now().date()))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    ax.plot(df['minute'], df['average'])
    plt.show()


def candlestick(ticker):
    
    ##def convert(s):
    ##    return datetime.strptime(s, '%Y-%m-%d %H:%M')
    ##d = convert('2019-02-10 05:33')
    ##print(d)
    ##d.toordinal()
    ##print(d)

    plt.style.use('ggplot')
    df = pd.DataFrame()
    ax = plt.subplot()
    ##df_date = pd.DataFrame()
    ##df_open = pd.DataFrame()
    ##df_high = pd.DataFrame()
    ##df_low = pd.DataFrame()
    ##df_close = pd.DataFrame()

    print(datetime.now().date())
    df = get_historical_intraday(ticker,output_format='pandas', token="<sk_1da2a30c93b740bab23ef61a5112f1da>")
    print(df.head())

    df = df[[ 'open', 'high', 'low', 'close']] 
    df = df.dropna(how='any')
    print(df.head())
    df = df.reset_index()
    print(df.head())
    ##df_date = df[['minute']]
    ##df_open = df[['open']]
    ##df_high = df[['high']]
    ##df_low = df[['low']]
    ##df_close = df[['close']]
    #data['Date2'] = data['Date'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
    #tuples = [tuple(x) for x in data[['Date2','Open','High','Low','Close']].values]

    df.to_csv('ohlc.csv')
    #df = pd.read_csv('ohlc.csv')
    #df = df[[ 'minute', 'open', 'high', 'low', 'close']] 

    df['minute'] = str(datetime.now().date())+ str(' ') + df['minute'].astype(str)
    #df['minute'] = pd.to_datetime(df['minute'])
    #df['minute'] = df['minute'].map(mdates.date2num)
    print(df.head())

    #ax1 = datetime.strptime("2019-02-10 05:33", '%Y-%m-%d %H:%M')
    #ax.xaxis.set_major_formatter(ax1)
    #df['minute'] = df['minute'].str.replace('-','')
    ##df['minute'] = df['minute'].str.replace(' ','')
    ##df['minute'] = df['minute'].str.replace(':','')
    ##df['minute'] = df['minute'].astype(float)
    #df['minute'] = float(datetime.strptime(df['minute'], '%Y-%m-%d %H:%M'))

    df['minute'] = pd.to_datetime(df['minute'])
    df['minute'] = df['minute'].apply(lambda d: mdates.date2num(d.to_pydatetime()))
    minlocator = mdates.MinuteLocator(byminute=[0,30]) 
    ax.xaxis.set_major_locator(minlocator)
    print(df.head())

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
    #ax.xaxis.set_major_formatter(num2date('%Y%m%d%H%M'))
    #ax.format_xdata = mdates.DateFormatter('%Y%m%d%H%M')
    #candlestick2_ohlc(ax, df_open, df_high, df_low, df_close)
    candlestick_ohlc(ax, df.values, width=0.0001 ,colorup='g')
    plt.title(ticker + '  ' + str(datetime.now().date()))
    ax.plot()
    plt.show()

#candlestick(ticker)
#chart("AAPL")


