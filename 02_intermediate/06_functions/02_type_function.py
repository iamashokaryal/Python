#One particularly interesting thing about Python is that not only can 
# we create custom objects,but every pre-existing thing 
# available in Python is an object, whether it's strings, lists, numbers or even functions.

number = 5

print(type(number))
# If we look at the output, we can see <class 'int'>. 
# It means, 10 is an object created from the int class.

numbers = [1,2,3,4]
print(type(numbers))

flag = True
print(type(flag))

def my_function():
    pass
print(type(my_function))

set1 = {1,2,3,4,5}

print(type(set1))