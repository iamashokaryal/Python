
#normal way
numbers = list()

for i in range(1,6):

    numbers.append(2**i)

print(numbers)


#using list comprehension

numbers1 = [2**i for i in range(1,6)]
print(numbers1)