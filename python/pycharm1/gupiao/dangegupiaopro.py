import pandas as pd
import tushare as ts
import threading
import time
import datetime
import matplotlib.pylab as plt

ts.set_token('acfe91c33583e4f34c757cfc5360f7e51eefd9f0c259f4204ea4720f')

time_temp = datetime.datetime.now() - datetime.timedelta(days=1)

pro = ts.pro_api()

start_dt = '20181021'

end_dt = time_temp.strftime('%Y%m%d')

df = pro.daily(ts_code='000001.SZ', start_date=start_dt, end_date=end_dt)