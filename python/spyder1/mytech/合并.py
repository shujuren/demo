#import tushare as ts
#import pandas as pd
#
##原始数据
#df=ts.get_hist_data \
#('000875',start='2018-12-01',end='2018-12-31')
##设这个是下载的新数据
#df1=df[0:10]
##设这个是老数据
#df2=df[5:]
##开始合并处理
#df3=df1.append(df2)
##去重
#df4=df3.drop_duplicates()

import tushare as ts

#原始数据
df=ts.get_hist_data \
('000875',start='2018-12-01',end='2018-12-31')
#设这个是下载的新数据
df1=ts.get_hist_data \
('000875',start='2018-12-21',end='2018-12-31')
#设这个是老数据
df2=ts.get_hist_data \
('000875',start='2018-12-01',end='2018-12-26')
#开始合并处理
df3=df1.append(df2)
#去重
df4=df3.drop_duplicates()