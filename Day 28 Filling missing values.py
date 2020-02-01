import numpy as np
import pandas as pd

#create a pandas DataFrame
d={'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[4,6,7]}
df=pd.DataFrame(d)
print(df)

#fill a null/missing value with default
print('\nFill default values in NULL/Missing values places')
print(df.fillna(value=0))

#fill a null/missing value with mean of that row/column
print('\nFill mean values in NULL/Missing values places')
print(df['A'].fillna(value=df['A'].mean()))
