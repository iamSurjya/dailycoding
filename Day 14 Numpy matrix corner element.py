import numpy as np

a=np.arange(16).reshape(4,4)
print(a)

#print the corner element of the array
print('\n Corner elements')
rows = np.array([[0,0],[3,3]])
cols = np.array([[0,3],[0,3]])
print(a[rows, cols])
