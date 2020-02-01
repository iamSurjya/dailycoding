import pandas as pd

# Creating the dataframe
df = pd.DataFrame({"A":[12, 4, 5, None, 1],
                   "B":[None, 2, 54, 3, None],
                   "C":[20, 16, None, 3, 8],
                   "D":[14, 3, None, None, 6]})
print('DataFrame')
print(df)

# to interpolate the missing values
print('\nTo interpolate the missing values(Column-by-Column)')
print(df.interpolate(method ='linear', limit_direction ='forward',axis=0))

print('\nTo interpolate the missing values(Row-by-Row)')
print(df.interpolate(method ='linear', limit_direction ='forward',axis=1))

print('\nMaximum number of consecutive missing to fill based on each axis')
print(df.interpolate(method ='linear', limit_direction ='forward',axis=1,limit=1))
