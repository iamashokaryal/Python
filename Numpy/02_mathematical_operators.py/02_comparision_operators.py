import numpy as np

array1 = np.array([1,2,3,4,5])

array2 = np.array([2,3,3,5,6])

result = array1 > array2

print(result)

result = array1 == array2

print(result)

# now using numpy functions 

result = np.less(array1,array2)
print(result)

result = np.greater(array1,array2)
print(result)

result = np.less_equal(array1,array2)
print(result)

result = np.greater_equal(array1,array2)
print(result)

result = np.not_equal(array1,array2)
print(result)


