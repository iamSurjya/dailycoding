import numpy as np
import pandas as pd
from numpy.random import rand


np.random.seed(101)
#creating an pandas DataFrame using an numpy array.
print('pandas DataFrame')
print(pd.DataFrame(rand(5,4),['A','B','C','D','E'],['W','X','Y','Z']))
