import numpy as np
x = np.array([[1, 2], [3, 4], [5, 6]])
print('Array')
print(x)

y = x[[0,1,2], [0,1,0]]
print('\nFrom each row, a specific element should be selected') #fetching [1 4 5]
print(y)

print('\nFrom a 4x3 array the corner elements should be selected using advanced indexing')
x = np.array(
[[ 0,  1,  2],
[ 3,  4,  5],
[ 6,  7,  8],
[ 9, 10, 11]])

y=x[[0,0,3,3],[0,2,0,2]]
#print(y)

print(x[[0,3],[1,2]])
