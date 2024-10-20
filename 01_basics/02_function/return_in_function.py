def addition(c,d):
    sum = c + d
    #find sum inside the function and print the result in outside the function
    #we can acheive that using return statement 
    #when we return a value it comes back to the function the we can assign this return value to a variable
    
    return sum 

#sum is return to the function call

a = 2
b = 3

sum = addition(a,b)

print(sum)

#when a return statement is encounter immediately the function terminates and 
# and control of the program goes to the place from where function is called. 