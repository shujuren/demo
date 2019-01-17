import tushare as ts
import pandas as pd

ts.set_token('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

pro = ts.pro_api()

df = pro.daily(ts_code='000001.SZ', start_date='20180101', end_date='20181231')

dfmonth = df.resample('Q').last()

