import tushare as ts
import numpy as np
import talib
 
#首先下载数据
data=ts.get_hist_data('600000',start='2018-01-01',end='2018-12-31')
 
data1=data[['open','low','high','close','volume']]
 
df=data1.sort_index()
 
close=np.array(df.close)
open=np.array(df.open)
low=np.array(df.low)
high=np.array(df.high)
vol=np.array(df.volume)

result = talib.MFI(high, low, close, vol, timeperiod=14)