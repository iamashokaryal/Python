# Exception handling is the process of responding to exceptions 
# in a custom way during the execution of a program.

# To use exception handling in Python, 
# we use the try...except block. 

# Inside the try block, we put the code that may raise an exception.
# Now if an exception occurs, the program jumps immediately to the except block.
# However, if exceptions do not occur, the except block is skipped.

try:

    numerator = int(input('Enter numerator:'))
    denominatior = int(input('Enter Denominator:'))

    result = numerator / denominatior

    print(result)

except:
    print('Denominator cannot be 0, Try again.')