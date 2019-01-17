import pandas as pd
import tushare as ts
import threading
import time
import datetime

api = ts.pro_api('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

#取000001的前复权行情
df = ts.pro_bar(pro_api=api, ts_code='000001.SZ', adj='qfq', start_date='20181201', end_date='20181231')

df1 = df[['open','high','open','close']]

index1 = [i for i in df1.index.format()]