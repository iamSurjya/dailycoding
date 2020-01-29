import pandas as pd
import numpy as np
from numpy.random import rand

df=pd.DataFrame(rand(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

#Writing data to a csv file
path_to_file = '/Users/surajchoudhary/documents/demo.csv'
df.to_csv(path_to_file,sep=",",mode='w',header=True,index=False)
print('File Created')
