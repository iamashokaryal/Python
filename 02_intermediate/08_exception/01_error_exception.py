# Types of Error :
# Two types: Syntax Error , Exception

# eg: if 5>3
         # print('a')

# Exception: Even if our code is syntactically correct, we may sometimes get an error.
# For example, if we divide a number by 0, we get an error.

#Types Of Exception :

# 1. IndexError Exception
# This exception occurs when the index we are using in a sequence 
# (list,tuple,string) is out of range

numbers = [1,2,3]

print(numbers[4]) # raises IndexError Exception

# 2. Key Error Exception

# This Exception occurs when a key is not found in a dictionary 

person = {'name': 'Ramesh', 'age':30}

print(person['profession']) #raises keyError Exception

#3. ValueError Exception 

# This excwption is occurs if a function or an operation is applied
# to an incorrect type.

import math

# raises TypeError Exception

a = math.sqrt('hello')

print(a)
