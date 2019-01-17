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

#首先下载数据
data=ts.get_hist_data('600000',start='2018-01-01',end='2018-12-31')

#要排序下数据，因为下载的数据排序是从近到远
df=data.sort_index()

#按照收盘价计算，所以取出收盘价
close= df.close

cangwei=0 #用于判断是否持仓，0代表空仓

# 计算5日的移动均线
ma5 = talib.MA(np.array(close), timeperiod=5)

# 计算60日的移动均线
ma60 = talib.MA(np.array(close), timeperiod=60)


#获得买卖的信号
SmaSignal=pd.Series(0,index=close.index)

for i in range(60,len(close)):
    if (ma5[i]>ma60[i] and ma5[i-1]<ma60[i-1] and cangwei==0):
        SmaSignal[i]=1
        cangwei=1
    if (ma5[i]<ma60[i] and ma5[i-1]>ma60[i-1] and cangwei==1):
        SmaSignal[i]=-1
        cangwei=0
        

#把信号,计算出来的线，close等整合到一个新的dataframe
final=pd.DataFrame({'close':close,'SmaSignal':SmaSignal,'ma':ma5,'ma60':ma60},index=close.index)        


#把有交易的天都取出来,这就是所有的买卖信号
sellorbuy=final[final['SmaSignal']!=0]

#必须复制出来一份，否则是在视图上操作，就报错
sellorbuy=sellorbuy.copy()


#计算收益
sellorbuy['balance']=sellorbuy['close'].diff()

#计算收益率
#把卖的那天取出来，因为买了卖了才有收益
sell=sellorbuy[sellorbuy['SmaSignal']==-1]
#最后计算总的收益率
sell['balance'].sum()


#这个不影响结果，就是让 result 买的时候余额为0
buy=sellorbuy[sellorbuy['SmaSignal']==1]
buy=buy.copy()
buy['balance']='NaN'
result = pd.concat([sell,buy]).sort_index()


#把下载的数据硬盘上，这样就能用SAS读取了
df.to_csv('p:/stock/day.csv',columns=['open','high','low','close'])