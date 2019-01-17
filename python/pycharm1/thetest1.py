# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:46:18 2018
研究均线策略

@author: 数据人
"""
import tushare as ts
import pandas as pd
import numpy as np
import talib
import matplotlib.pylab as plt

#首先下载数据
ts.set_token('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

pro = ts.pro_api()

df1 = pro.daily(ts_code='000875.SZ', start_date='20180101', end_date='20181231')