def add_numbers(*numbers):
    total = 0
    for n in numbers:

        total = total + n

    return total

result = add_numbers(5,10)

print(result)

result = add_numbers(5,10,20)

print(result)