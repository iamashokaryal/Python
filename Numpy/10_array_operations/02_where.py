# The NumPy where() method finds indices that are true in an array based on a given condition.

# Let's say we want to replace all negative elements from an array with value 0, we can use np.where() in the following way:

import numpy as np

arr = np.array([[1,2],[3,4]])

print(np.where(arr<0,arr,1))

# condition true vako print garxa, baki paxadi ko anusar change garxa