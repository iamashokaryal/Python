import numpy as np

mat1 = np.array([[1,2],
                 [3,4]])
mat2 = np.array([[5,6],
                 [7,8]])
# this use matrix rule like (1*5+2*7 = 19) for 1st result
result1 = np.transpose(mat1)

result2 = np.transpose(mat2)

print(result1)
print(result2)