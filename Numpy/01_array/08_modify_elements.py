import numpy as np

# Here, numbers[numbers % 2 == 0] accesses all even numbers 
# of the numbers array and then we have assigned 0 to those numbers.

numbers = np.array([1,2,3,4,5,6,7])

numbers[numbers%2 ==0]=0

print(numbers)