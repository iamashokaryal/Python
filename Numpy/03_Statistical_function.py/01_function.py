
import numpy as np 


marks = np.array([70,80,65,78,58,96,60])

# returns the mean of an array
mean_marks = np.mean(marks)

print(f"Mean marks is :{mean_marks}")

# returns the median of an array
median_marks = np.median(marks)

print(f"median of marks is :{median_marks}")

# returns the standard deviation of an array
standard_deviation = np.std(marks)

print(f'Standard deviation is: {standard_deviation}')

# returns the nth percentile of elements in an array
percentile1 = np.percentile(marks,1)

print(f'Percentile of marks is {percentile1}')

# returns the minimum element of an array
minimum = np.min(marks)

print(f'minimum element of the array is : {minimum}')

# returns the maximum element of an array
maximum = np.max(marks)
print(f'maximum element of the array is : {maximum}')






