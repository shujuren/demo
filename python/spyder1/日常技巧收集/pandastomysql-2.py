# -*- coding: utf-8 -*-
import tushare as ts
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine \
('mysql+pymysql://root:root@localhost:3306/test?charset=utf8')

#设这个是老数据
df=ts.get_hist_data \
('000875',start='2018-12-01',end='2018-12-26')

df['date'] = pd.to_datetime(df.index)

df.to_sql('day', con=engine,if_exists='replace',index=False)

#设这个是老数据
df=ts.get_hist_data \
('000875',start='2018-12-20',end='2018-12-31')

df['date'] = pd.to_datetime(df.index)

df.to_sql('day', con=engine,if_exists='append',index=False)


engine.execute("CREATE TABLE abc AS (SELECT DISTINCT * FROM day ORDER BY date)")

engine.execute("DROP TABLE day")

engine.execute("RENAME TABLE abc TO day")

sql="SELECT * FROM day"

alldf=pd.read_sql(sql,con=engine,index_col='date')