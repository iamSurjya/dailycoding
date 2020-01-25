import numpy as np
import pandas as pd
from numpy.random import rand

np.random.seed(101)
#creating an column pandas DataFrame using an numpy array.
print('pandas DataFrame')
df=pd.DataFrame(rand(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#adding row in to pandas.DataFrame
df.loc['F']=[0.2345,0.4567,0.6789,0.7890]
print(df)

#adding row in to pandas.DataFrame with same elemet
df.loc['G']='12345'

#droping row from pandas DataFrame
print('\nDrop row from DataFrame')
df.drop('G',axis=0)
print(df)

print('\nDrop row from DataFrame with explicitly specify to delete')
df.drop('G',axis=0,inplace=True)
print(df)
