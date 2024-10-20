# A try statement can also have an optional finally block which is executed regardless of 
# whether an exception occurs or not. For example,

try:
    print(1/0)

except:
    print('wrong denominator')

finally:
    print('Always printed')

# Here's how this code works:

# The code inside the try block raises an exception.
# Hence, the except block is executed.
# Then, the finally block is executed.


try:
    print(1/2)

except:
    print('exception occur!')

finally:
    print('Printed.')
 
# If the try block didn't raise any exception, the except block gets skipped. 
# However, the finally block still gets executed.

#What's the use of finally?

# The finally block is used to perform cleanup actions 
# that need to be executed under all circumstances.

#Suppose, we are working with an external file in our program. 
# We need to close this file at the end even if an exception occurs.

#In such cases, we put the code to close the file inside the finally block. 
# We will cover this example in our Files lesson.