import numpy  as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

#How to vertically concatenate two arrays in Python
print('Method 1')
print(np.concatenate([a, b], axis=0))

print('\nMethod 2')
print(np.vstack([a, b]))

#How to horizontally concatenate two arrays in Python
print('\nMethod 1')
print(np.concatenate([a, b], axis=1))

print('\nMethod 2')
print(np.hstack([a,b]))
