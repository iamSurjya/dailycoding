import numpy as np
import pandas as pd
from numpy.random import rand

np.random.seed(101)
#creating an column pandas DataFrame using an numpy array.
print('pandas DataFrame')
df=pd.DataFrame(rand(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#adding new column to an Existing DataFrame
df['new']=0.233333
print('\nAdding new column to an Existing DataFrame')
print(df)

#adding a new column based on 2 existing columns
print('\nAdding new column to an Existing DataFrame based on existing columns')
df['new']=df['W']+df['Z']
print(df)

#droping column from pandas DataFrame
print('\nDrop column from DataFrame')
df.drop('W',axis=1)
print(df)

print('\nDrop column from DataFrame with explicitly specify to delete')
df.drop('W',axis=1,inplace=True)
print(df)
