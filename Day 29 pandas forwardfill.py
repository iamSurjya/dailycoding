import numpy as np
import pandas as pd

#create a pandas DataFrame
d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[np.nan,6,7]}
df=pd.DataFrame(d)
print(df)

#fill the missing values in column
print('\nFill the missing values in column')
print(df.ffill(axis=0))

#fill the missing values in row
print('\nFill the missing values in row')
print(df.ffill(axis=1))
