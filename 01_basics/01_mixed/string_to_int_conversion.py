#this is the example of Explicit conversion 
#In Explicit Type Conversion, users convert the data type of an object to required data type.

#We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.

#This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

num_string = '15'
num_int = 23
print(type(num_string)) #gives string

#string to int conversion 
num_string = int(num_string)

print(type(num_string)) #gives int output

sum = num_string + num_int

print("sum:", sum)