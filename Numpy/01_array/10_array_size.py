import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])

arr1 = np.array([1,2,3,4,5,6,7,8], dtype=np.int32)

print(f"size of the array is :{arr.size}")

# specifies the number of dimensions of an array (for 1D array, it is 1)
print(f"dimension of the array :{arr.ndim}")

# returns the size of the array in each dimension (for 1d array, it is the length of the array)

print(f"shape in one dimension :{arr.shape}")

# specifies the data type of elements of the array (float, int, or complex)
print(f"type of the array :{arr.dtype}")

# represents the size in bytes of each element of the array

print(f"size in bytes of the each elements in array :{arr.itemsize}")
print(f"size in bytes of the each elements in array1 :{arr1.itemsize}")

# represents total size in bytes of the array (nbytes = itemsize * size)

print(f"total size of the array :{arr.nbytes}")
print(f"total size of the array1 :{arr1.nbytes}")




