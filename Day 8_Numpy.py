#program to convert temperature from Celsius to Fahrenheit using numpy array

import numpy as np

#temperature data stored in list
temperature_in_Celsius=[20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]

#formula is (0°C × 9/5) + 32 = 32°F

# calculating using list
print('Calculating using list')
temperature_in_Fahrenheit=[num*9/5+32 for num in temperature_in_Celsius]
print(temperature_in_Fahrenheit)

# calculating using numpy array
print('\nCalculating using numpy array')
temperature_in_Fahrenheit=(np.array(temperature_in_Celsius)*9/5+32)
print(temperature_in_Fahrenheit)
