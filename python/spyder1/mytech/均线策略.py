# -*- coding: utf-8 -*-
"""

"""

import tushare as ts
import pandas as pd
import numpy as np
import talib

#首先下载数据
data=ts.get_hist_data('000875',start='2018-01-01',end='2018-12-31')

#要排序下数据
df=data.sort_index()

#按照收盘价计算，所以取出收盘价
close= df.close


# 计算5日的移动均线
ma5 = talib.MA(np.array(close), timeperiod=5)

# 计算10日的移动均线
ma60 = talib.MA(np.array(close), timeperiod=60)


#获得买卖的信号
SmaSignal=pd.Series(0,index=close.index)

for i in range(10,len(close)):
    if (ma5[i]>ma60[i] and ma5[i-1]<ma60[i-1]):
        SmaSignal[i]=1
    if (ma5[i]<ma60[i] and ma5[i-1]>ma60[i-1]):
        SmaSignal[i]=-1
        

#把买卖的信号和原来的数据整合的一起        
df['SmaSignal']=SmaSignal

#形成一个新的数据框  
df1=df[['close','SmaSignal']]
df1['ma5']=ma5;
df1['ma60']=ma60;


#把有交易的天都取出来
sellorbuy=df1[df1['SmaSignal']!=0]

#计算收益
sellorbuy['balance']=sellorbuy['close'].diff()

#把卖的那天取出来，因为买了卖了才有收益
sell=sellorbuy[sellorbuy['SmaSignal']==-1]
#最后计算总的收益率
sell['balance'].sum()


#保存到硬盘上，这样就能用SAS读取了
df.to_csv('p:/day000875.csv',columns=['open','high','low','close'])
