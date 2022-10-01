from nse_custom_candlestick_data import ohlcDataFrames, ohlcDataFrameForOneYear, ohlcDataFrameForOneYearPerDay
import datetime as dt
import pandas as pd


# list_of_df = ohlcDataFrameForOneYear()
# print(len(list_of_df))

# tf1 = list_of_df[0]
# tf1['tmp'] = tf1.index
# tf1[["day", "time"]] = tf1["tmp"].astype(str).str.split(expand=True)
# df1 = tf1.groupby(["day"])
# #l = [df1.get_group(x) for x in df1.groups]

# print(df1.groups.keys())

# for  x in df1.groups:
# 	print(x)
# 	print(df1.get_group(x))
# 	print(type(df1.get_group(x)))
# 	print("*************************************")

import pprint
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(ohlcDataFrameForOneYearPerDay())