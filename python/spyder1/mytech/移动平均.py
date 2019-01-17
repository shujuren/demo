# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 10:04:23 2018

@author: WZY
"""

import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import talib

#首先下载数据
data=ts.get_hist_data('000875',start='2018-01-01',end='2018-12-31')

#要排序下数据
df=data.sort_index()

#按照收盘价计算，所以取出收盘价
close= df['close'].tolist()

buy=[]
sell=[]
a=0 #用于判断是否持仓，0代表空仓
ret=0

nrows = len(close) #行数

Sma=[0.0 for i in range(nrows)]

 
for j in range(19,nrows):#计算20日均线数值
    Sma[j]=sum(close[(j-19):(j+1)])/20
    
for k in range(19,nrows): #收盘价在20日均线之上，且均线是向上的，空仓的时候买入
    if Sma[k-1]<Sma[k] and close[k]>Sma[k] and a==0:
        buy.append(close[k])
        a=1
    elif close[k]<Sma[k] and Sma[k]<Sma[k-1] and a==1:#收盘价在20日均线之下，且均线是向下的，持仓的时候卖出   
        sell.append(close[k])
        a=0
        
for l in range(0,len(sell)):  #用卖出数列减去买入数列得到收益点数，然后对所有收益求和
    ret += sell[l]-buy[l]
print("总的收益点数：" "%.2f"% ret) #总的收益点数,绝对数值，不是百分比
plt.ylim(2000,6000)
plt.plot(Sma[0:len(Sma)],'r')
plt.plot(close,'k')
plt.show()
     

