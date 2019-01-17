import tushare as ts
import pandas as pd
#
##通过去重进行合并
##原始数据
#df=ts.get_hist_data \
#('000875',start='2018-12-01',end='2018-12-31')
##设这个是下载的新数据
#df1=ts.get_hist_data \
#('000875',start='2018-12-21',end='2018-12-31')
##设这个是老数据
#df2=ts.get_hist_data \
#('000875',start='2018-12-01',end='2018-12-26')
#
#df2.to_csv('p:/abc.csv',index=True)
#
#df21=pd.read_csv('p:/abc.csv',index_col='date')
##开始合并处理
#df3=df1.append(df21)
##去重
#df4=df3.drop_duplicates()


#通过索引进行合并
#原始数据
df=ts.get_hist_data \
('000875',start='2018-12-01',end='2018-12-31')
#设这个是下载的新数据
df1=ts.get_hist_data \
('000875',start='2018-12-21',end='2018-12-31')
#设这个是老数据
df2=ts.get_hist_data \
('000875',start='2018-12-01',end='2018-12-26')

df2.to_csv('p:/abc.csv',index=True)
df21=pd.read_csv('p:/abc.csv',index_col='date')

#开始合并处理
df3=df1.append(df21)
#去重
df4=df3.groupby(level=0).mean()