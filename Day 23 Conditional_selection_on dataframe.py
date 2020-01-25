import numpy as np
import pandas as pd
from numpy.random import rand

np.random.seed(101)
#creating an column pandas DataFrame using an numpy array.
print('pandas DataFrame')
df=pd.DataFrame(rand(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#Conditional Selection
print('\nCheck if DataFrame satisfy given condition')
print(df>0.5)

print('\nReturn a DataFrame after matching the condition')
print(df[df>0.3])

print('\nKeep only the rows that satisy the condition')
print(df[df['W']>0.3])
