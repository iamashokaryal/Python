
import numpy as np

matrix1 = np.array([[1,2],
                    [2,3]])

print('\n',matrix1)

# create a prefilled matrix

one_matrix = np.ones((3,3))

print(one_matrix)

# using np.matrix

matrix2 = np.matrix([[1,2],[35,5]])

print(matrix2)

# the matrix created by np.array() and np.matrix() is the same.

# However, there is one main difference between arrays and matrices in NumPy.