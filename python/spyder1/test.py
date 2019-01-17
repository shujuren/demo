import pandas as pd
import numpy as np
import talib

price = [22.2734,22.194,22.0847,22.1741,22.184,22.1344,22.2337,22.4323,22.2436,22.2933,22.1542
,22.3926,22.3816,22.6109,23.3558,24.0519,23.753,23.8324,23.9516,23.6338,23.8225,23.8722,23.6537,23.187
,23.0976,23.326,22.6805,23.0976,22.4025,22.1725]

close=np.array(price)

ta_ma5 = talib.SMA(close,timeperiod=5)

#用pandas计算
df=pd.DataFrame(price)

pd_ma5=df.rolling(5).mean()