import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(arr)

# [row_start:row_end , column_start:column_end]
print('after slicing \n',arr[:2,:])

print(arr[0:2,0:2])