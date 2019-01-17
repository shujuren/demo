import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv('d:/class.csv',encoding='gbk',header=0))

df1=pd.DataFrame(df['Height'])
df2=pd.DataFrame(df['Weight'])

dtvalue1 = [i[0]*10 for i in df1.values]
dtvalue2 = [i[0]*10 for i in df2.values]

aa = [dtvalue2,dtvalue2]