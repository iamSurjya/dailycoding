import numpy as np
import pandas as pd
from numpy.random import rand


np.random.seed(101)
#creating an pandas DataFrame using an numpy array.
print('pandas DataFrame')
df=pd.DataFrame(rand(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

#access column from a DataFrame
print(df['W'])
print(type(df['W']))#Return the type of data

#access multiple columns
print(df[['W','Z']])
print(type(df[['W','Z']]))#Return the type of data
