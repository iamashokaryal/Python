import numpy as np

# it gives random integer between 1 to 100

random_number = np.random.randint(1,100)

print(random_number)

# 1 to 100 ko 5 wota random dinxa
random_number = np.random.randint(1,100,5)

print(random_number)

# array creation using np.random.rand()
# NumPy has the function called np.random.rand() 
# to create an array of random numbers between 0 and 1.

array1 = np.random.rand(4)

print(array1)

