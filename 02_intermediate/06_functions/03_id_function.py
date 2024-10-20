# every object has an id for identity. The id of an object is always unique 
# and constant for this object during its lifetime.

number1 = 5

print(id(number1))

number2 = 10

print(id(number2))

#As we can see, the id of number1 and number2 are different. 
# It means they are two different objects.

number3= number2
print(id(number3))

#The id() function returns the identity of the given object. 
# If the ids of two objects are the same, that means they are referring to the same object.

