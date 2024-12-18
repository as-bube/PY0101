# import numpy library

import numpy as np 

a = np.array([0, 1, 2, 3, 4])

# print(np.__version__)
# print(a.dtype)

# b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
# print(b.dtype)

# Create numpy array

c = np.array([20, 1, 2, 3, 4])
c[0] = 100
# print(c)

d = np.array([10, 2, 30, 40,50])

d[1:3] = 33, 44

# print(d)
# print(d[1:4:2])

''''
    Numpy Statistical Functions
'''

a = np.array([1, -1, 1, -1])

# print(a)

# Get the mean of numpy array

mean = a.mean()
# print(mean)

# Get the standard deviation of numpy array

standard_deviation=a.std()
# print(standard_deviation)

# Get the biggest value in the numpy array

max_a = a.max()
# print(max_a)

# Get the smallest value in the numpy array

min_a = a.min()
# print(min_a)

c = np.array([-10, 201, 43, 94, 502])
min_c = c.min()
max_c = c.max()

# print(min_c + max_c)

'''
    Numpy Array Operations
'''


    