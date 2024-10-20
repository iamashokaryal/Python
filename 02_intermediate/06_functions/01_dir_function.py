#In Python, everything is an object.

# The dir() function lists out all the attributes and methods of the given object.

# example 

number = 1

print(dir(number))

# in outuput we see that one __add__ method, lets use this

number = 5

result = number.__add__(100)

print(result) #gives outuput 105

# As we can see, the __add__() method can be used for addition.

# In fact, the + operator internally calls this __add__() method for addition.

# At the surface, it may look like the + operator is working like how it works in mathematics, 
# but internally it's calling the __add__() method for addition.