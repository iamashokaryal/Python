# Get the Largest Item

# method 1

numbers = [1,2,3,5,7,8,9]

largest = numbers[0]

for num in numbers:
    if largest < num:
        largest = num

print (largest)

# method 2

large_num = max(numbers)

print(large_num)