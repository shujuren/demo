import pandas as pd
import numpy as np

index = pd.date_range('3/8/2017', periods=6, freq='M')
df1 = pd.DataFrame(np.random.randn(6), index=index)
df2 = pd.DataFrame(np.random.randn(6), index=index)

dtvalue1 = [i[0] for i in df1.values]
dtvalue2 = [i[0] for i in df2.values]
index1 = [i for i in df1.index.format()]





