
import pandas as pd

print('pandas.Series')
data=pd.Series(['a','b','c'])
print(data)

#creating a series using an list
print('\nCreating series using list')
list=['10','19','20','29']
print(pd.Series(list))

#creating a series using list with index as letters
print('\nCreating series using list with index as letters')
labels=['a','b','c','d']
print(pd.Series(list,labels))

#creating list using a dictionary
dict={'a':10,'b':20,'c':30,'d':40}
print(pd.Series(dict))
