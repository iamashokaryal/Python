def add_numbers(n1=500, n2 = 1000):
    sum = n1+n2

    return sum 

sum = add_numbers(5.4)
print(sum)

#here n1 and n2 are two paramenter and has a default value 
#we have providing 5.4 as an argument, that value will pass to n1, however we had not provided a
# second argument so default value of n2 will be used
# if we remove 5.4, default value of both n1 & n2 will be used 