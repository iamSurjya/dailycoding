import numpy as np
import pandas as pd
from numpy.random import rand

np.random.seed(101)
#creating an column pandas DataFrame using an numpy array.
print('pandas DataFrame')
df=pd.DataFrame(rand(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#Show how python and operator throws and ValueError.
#print(df[df['W']>0.3 and df['Z']>0.2])

#Use of & to execute conditional statement with multiple conditions.
print('\nUse of & in coditional selection')
print(df[(df['W']>0.3) & (df['Z']>0.2)])

print('\nUse of | in coditional selection')
print(df[(df['W']>0.3) | (df['Z']>0.2)])
