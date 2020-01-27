import pandas as pd
import numpy as np
from numpy.random import rand

df=pd.DataFrame(rand(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

print('\nReset Index of an DataFrame')
print(df.reset_index())

print('\n Set a column as index')
print(df.set_index('Y'))

print('\n Re-Index DataFrame')
new_index='B C D A E'.split()
print(df.reindex(new_index))

df=df.reindex(new_index)
print(df)
