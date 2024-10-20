import numpy as np

arr1 = np.array([[1,2],
                 [3,4]])
arr2 = np.array([[5,6],
                 [7,8]])
# In NumPy arrays, the * operator performs element-wise multiplication.
# So, corresponding elements of arr1 and arr2 are multiplied:

print(arr1*arr2)

mat1 = np.matrix([[1,2],
                 [3,4]])
mat2 = np.matrix([[5,6],
                 [7,8]])
# this use matrix rule like (1*5+2*7 = 19) for 1st result
print(mat1*mat2)
