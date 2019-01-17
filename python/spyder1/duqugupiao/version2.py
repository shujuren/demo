# -*- coding: utf-8 -*-
import pandas as pd
import tushare as ts
import threading
import time
import datetime
from sqlalchemy import create_engine 

engine = create_engine \
('mysql+pymysql://root:root@localhost:3306/test?charset=utf8')

ts.set_token('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

pro = ts.pro_api()

time_temp = datetime.datetime.now() - datetime.timedelta(days=1)

start_dt = '20181201'

end_dt = '20181226'

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

code = data.ts_code.tolist()

dataname=code[0].replace('.SZ', '')

#设这个是老数据
df = pro.daily(ts_code=code[0], start_date=start_dt, end_date=end_dt)

df.to_sql('day'+dataname, con=engine,if_exists='replace',index=False)

#设这个是新数据
start_dt = '20181221'

end_dt = time_temp.strftime('%Y%m%d')

df = pro.daily(ts_code=code[0], start_date=start_dt, end_date=end_dt)

df.to_sql('day'+dataname, con=engine,if_exists='append',index=False)

sql="drop table if exists abc"

engine.execute(sql)

sql="CREATE TABLE abc AS (SELECT DISTINCT * FROM day"+dataname+" ORDER BY trade_date)"

engine.execute(sql)

sql="drop TABLE day"+dataname

engine.execute(sql)

sql="RENAME TABLE abc TO day"+dataname

engine.execute(sql)








