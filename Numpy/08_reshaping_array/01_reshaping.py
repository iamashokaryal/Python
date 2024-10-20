import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr1 = np.array([1,2,3,4,5,6,7,8])

# syntax = np.reshape(array_name,(req_row,req_column))
twoD = np.reshape(arr,(3,4))
print(twoD)

threeD = np.reshape(arr1,(2,2,2))

print(threeD)