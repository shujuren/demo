import pandas as pd
import tushare as ts
import threading
import time
import datetime

ts.set_token('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

pro = ts.pro_api()

time_temp = datetime.datetime.now() - datetime.timedelta(days=1)

start_dt = '20181221'

end_dt = time_temp.strftime('%Y%m%d')

data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')

code = data.ts_code.tolist()

changdu=100

def getdata():
    for i in range(changdu):
        df = pro.daily(ts_code=stock_pool[i], start_date=start_dt, end_date=end_dt)
        lujing = 'p:/stock/day' + stock_pool[i] + '.csv'
        df.to_csv(lujing, columns=['open', 'high', 'low', 'close'])

for j in range(6,30):
    stock_pool = code[j * changdu:(j + 1) * changdu]
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    timer = threading.Timer(60, getdata)  # 等待60s钟调用一次fun_timer() 函数
    timer.start()
    timer.join()