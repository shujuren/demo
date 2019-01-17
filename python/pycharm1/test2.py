# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

conn = create_engine('mysql+pymysql://root:root@localhost:3306/test?charset=utf8')
sql = 'select * from abc'
df = pd.read_sql(sql, con=conn)
print(df.head())

df = pd.DataFrame()
df["A"] = [1,2,3,4]
df["B"] = [11,22,33,44]
df.to_sql('abc1',con=conn,if_exists='replace',index=False)