#lambda function doesnot have a name
# the body of a lamda function  can have only one expression

#normal way

def double(n):
    return n*2

print(double(10))


#using lambda function 

double = lambda n:n*2  # function_name = lamda argument : return_value

print(double(10))


squre = lambda n: n**2

print(squre(9))