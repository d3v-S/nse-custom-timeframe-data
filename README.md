# nse-custom-timeframe-data

This script allows one to download candlestick data from Moneycontrol and EconomicTimes at realtime with per minute granularity.
Data can be taken both in json and pandas dataframe format.


## Usage:

- ```ohlcDataFrames```
- for using EconomicTimes as source, put symbolname that is used by EconomicTimes. Generally for stocks it is *.EQ* at the end.
- by default it uses Moneycontrol to get data. EconomicTimes seems to miss a minute or two here and there. 


## Features:
- Realtime data from moneycontrol and economictimes
- Any timeframe one likes
- in pandas dataframe and json format.
