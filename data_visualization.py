import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('df1', index_col=0)
df2 = pd.read_csv('df2')

df1_head = df1.head()
# print (df1_head)
df1['A'].hist()
# plt.show()