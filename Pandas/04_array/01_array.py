import pandas as pd

data = [2,3,4,5]

array1 =  pd.array(data)

array2 = pd.array([1,2,3,4])

print(array1)
print('------------------------------------')
print(array2)

# Explicitly Specify Array Elements Data Type
# # creating a pandas.array of integers

array3 = pd.array([40,50,60], dtype='int')

print('------------------------------------')

print(array3)

# creating a pandas.array of floating-point numbers

array4 = pd.array([1.1,2.2,3.4], dtype='float')
print('------------------------------------')

print(array4)