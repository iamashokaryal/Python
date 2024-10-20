# A function that calls itself is known as a recursive function. 
# And, this process is known as recursion.

def print_variable():

    text = 'hello'

    print(text)

#recursive call

    print_variable() # call the function inside the same function

print_variable() #normal function call