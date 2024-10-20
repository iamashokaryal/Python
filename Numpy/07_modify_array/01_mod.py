import numpy as np

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# changing the value of second row and 2nd element.

arr[1,1]= 55

print(arr)

arr[1,:]= 10

print(arr)

