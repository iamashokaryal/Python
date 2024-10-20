import numpy as np

mat1 = np.matrix([[1,2],
                 [3,4]])
mat2 = np.matrix([[5,6],
                 [7,8]])
result = np.dot(mat1,mat2)

print(result)

mat1 = np.array([[1,2],
                 [3,4]])
mat2 = np.array([[5,6],
                 [7,8]])
result = np.dot(mat1,mat2)

print(result)