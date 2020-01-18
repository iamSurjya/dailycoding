import pandas as pd

file_path='/Users/surajchoudhary/Documents/'
file_name='Test_import.csv'

#read data from a csv file.
data=pd.read_csv(file_path+file_name)
print('Original CSV')
print(data)

#reading only specific no of rows
data=pd.read_csv(file_path+file_name,nrows=3)
print('\n\nReading only specific no of rows')
print(data)

#Skip no of skiprows from top
data=pd.read_csv(file_path+file_name,skiprows=1)
print('\n\nSkip no of skiprows from top')
print(data)

#read specific columns
data=pd.read_csv(file_path+file_name,usecols =['first_name','age'])
print('\n\nReading specific Columns')
print(data)
