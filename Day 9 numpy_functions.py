import numpy as np

#creating an emppty array
print('Empty array')
print(np.empty((2,2)))

#creating a array with random values
print('\nRandom array')
print(np.random.random((2,2)))

print('\nArray of Zeros')
print(np.zeros((2,2)))

print('\nArray of ones')
print(np.ones((2,2)))

print('\nArray of number specified')
print(np.full((2,2),4))

print('\nIdentity Matrix')
#print(np.eye(2))  or
print(np.identity(2))

print('\nEvenly spaced Matrix')
print(np.linspace((2,2),3,num=5))
