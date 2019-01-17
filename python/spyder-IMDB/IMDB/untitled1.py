from pyecharts import Kline

import tushare as ts


api = ts.pro_api('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

#取000001的前复权行情
df = ts.pro_bar(pro_api=api, ts_code='000001.SZ', adj='qfq', start_date='20181201', end_date='20181231')

df = df.sort_index(axis=0)


df1 = df[['open','high','open','close']]

v1 = df1.values.tolist()
kline = Kline("K 线图示例")

aa = [i for i in df1.index.format()]

kline.add("日K", aa, v1)
kline.render()