# -*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
from sqlalchemy import create_engine

#设这个是老数据
df=ts.get_hist_data \
('000875',start='2018-12-01',end='2018-12-26')

df['date'] = pd.to_datetime(df.index)

engine = create_engine \
('mysql+pymysql://root:root@localhost:3306/test?charset=utf8')


df.to_sql('day', con=engine,if_exists='replace',index=False)

