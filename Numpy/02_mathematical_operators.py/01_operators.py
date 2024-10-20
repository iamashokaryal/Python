import numpy as np

array1 = np.array([1,2,3,4,5])

array2 = np.array([2,3,4,5,6])

# using + operator 
sum1 = array1 + array2

print(f'sum is {sum1}')

# using add() function 

sum2 = np.add(array1,array2)

print(f"sum is {sum2}")

# using subtract() function 

diff = np.subtract(array1 ,array2)

print(f'difference is {diff}')

# using divide() function 

division = np.divide(array1,array2)

print(f"Divison is {division}")

# what is it occur divide by zero

array3 = np.array([1,2,3,4,5])
array4 = np.array([0,2,4,3,6])

divide = np.divide(array3,array4)

print(f'divide by zero {divide}')


# using power() function 

power = np.power(array3,array4)

print(f'power {power}')
