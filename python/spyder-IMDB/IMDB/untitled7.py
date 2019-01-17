import pandas as pd
import numpy as np

df = pd.DataFrame(pd.read_csv('d:/class.csv',encoding='gbk',header=0))
df1 = df[df["Sex"]=="女"]
df2 = df[df["Sex"]=="男"]

dtvalue11 = df1['Height'].values.tolist()
dtvalue12 = df1['Weight'].values.tolist()

dtvalue121 = df2['Height'].values.tolist()
dtvalue122 = df2['Weight'].values.tolist()

x_axis = ['Height', 'Weight']
y_axis1 = [dtvalue11,dtvalue12]
y_axis2 = [dtvalue21,dtvalue22]

boxplot.add("category1", x_axis, boxplot.prepare_data(y_axis1))
boxplot.add("category2", x_axis, boxplot.prepare_data(y_axis2))

