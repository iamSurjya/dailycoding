import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print('Original series')
print(s)

#retrive data using label
print('\nRetrive data using label')
print(s['d'])

#Retrieve multiple elements using a list of index label values.
print('\nRetrieve multiple elements using a list of index label values')
print(s[['a','b','c']])

#Retrieve top 4 records of the series
print('\nRetrive top n elements from series')
print(s.head(4))

#Retriving data between 3 and 6
print('\nRetriving data between 3 and 6')
print(s.iloc[3:6])
