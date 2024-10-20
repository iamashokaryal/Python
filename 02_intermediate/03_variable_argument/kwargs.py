
# It's also possible to pass a variable number of keyword arguments in Python. 
# To accept these arguments in the function definition, we use ** before the argument name.

def print_info(**person):

    print(person)

print_info()

print_info(name = 'Steve')  # this gives output in dictionary

print_info(name= 'steve',age=29)
