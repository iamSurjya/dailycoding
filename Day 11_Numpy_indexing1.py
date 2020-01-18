#array indexing

import numpy as np
#creating an array 1-10
x=np.arange(1,10)
print('Base array')
print(x)

#slicing starting from 2 upto 7(not including the value on index 7)
print('\nSlicing')
print(x[2:7:2])

#reading data  on index -3 going upto 2 taking -2 step at a time
print('\nSlicing with negative index')
print(x[-3:1:-1])

print('\nAll after')
print(x[7:])

print('\nAll before')
print(x[:7])
