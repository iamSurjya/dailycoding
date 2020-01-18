import numpy as np

#Create a 3X4 matrix
a=np.arange(12).reshape(3,4)
print('Original Matrix')
print(a)

#check if the array elements are greater than 4.
print('\nCheck if matrix element is greater than 4')
print(a>4)

#check if the array elements are even.
print('\nCheck if the array elements are even')
print(a%2==0)

#Check if there is at least one element satisfying the condition
print('\nCheck if there is at least one element satisfying the condition')
print(np.any(a>4))

#Check if there all element satisfying the condition
print('\nCheck if there all element satisfying the condition')
print(np.all(a>100))
