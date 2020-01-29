import numpy as np
import pandas as pd

#create a pandas DataFrame
d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[4,6,7]}
df=pd.DataFrame(d)
print(df)

#drop rows with Null or missing values
print('\nDrop row with one or more Null/Missing values')
print(df.dropna())

#drop columns with Null or missing values
print('\nDrop columns with one or more Null/Missing values')
print(df.dropna(axis=1))

#Only drop rows when the row contains 2 or more Null/Missing values
print('\nDrop rows when the row contains 2 or more Null/Missing values')
print(df.dropna(thresh=2))
