
# we have passed *message as parameter. * before the argument name
# suggests that it's a variable argument and it will always be a tuple

def greet(*messages):

    print(messages)

greet('Hi')         # output tuple maa aauxa

greet('Hi', 'Hello') # output tuple maa aauxa

greet()               # output tuple maa aauxa

