import numpy as np

#creating array
x=np.ones((2,3)) # Creates a array of all ones
y=np.random.random((2,3)) #creates a array of a random numbers

#Array operations
print('Addition')
print(np.add(x,y)) #print(x+y)

print('Subtract')
print(np.subtract(x,y))

print('Multiply')
print(np.multiply(x,y))

print('Divide')
print(np.divide(x,y))

print('Remainder')
print(np.remainder(x,y))

print('Square Root')
print(np.sqrt(x))
