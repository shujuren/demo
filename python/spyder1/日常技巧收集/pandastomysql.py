# -*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine \
('mysql+pymysql://root:root@localhost:3306/test?charset=utf8')

df = pd.DataFrame({'name' : ['User 1', 'User 2', 'User 3']})

df.to_sql('users', con=engine,if_exists='replace')

df1 = pd.DataFrame({'name' : ['User 4', 'User 5']})
df1.to_sql('users', con=engine, if_exists='append')

engine.execute("SELECT * FROM users").fetchall()










#sql = 'select * from abc'
#df = pd.read_sql(sql, con=conn)
#print(df.head())
#
#df = pd.DataFrame()
#df["A"] = [1,2,3,4]
#df["B"] = [11,22,33,44]
#df.to_sql('abc1',con=conn,if_exists='replace',index=False)

