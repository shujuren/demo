from pyecharts import Bar, Grid

title = "Height For Class"
df = pd.DataFrame(pd.read_csv('d:/class.csv', encoding='gbk', header=0))

df1 = pd.DataFrame(df['Height'])
df2 = pd.DataFrame(df['Name'])

dtvalue1 = [i[0]  for i in df1.values]

index1 = [i[0] for i in df2.values.tolist()]



grid = Grid()

bar = Bar(title, "Height For Class")
bar.add('Height', index1, dtvalue1, is_datazoom_show=True, xaxis_interval=0, xaxis_rotate=30)
grid.add(bar, grid_bottom="25%")
grid.render()