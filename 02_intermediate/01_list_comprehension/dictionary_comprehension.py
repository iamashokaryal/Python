numbers = [1,2,3,4,5]

squre_numbers ={}

for num in numbers:
    squre_numbers[num] = num**2

print(squre_numbers)

#squre_numbers[key] = value, tei vayera automatic print hunxa
# key ra value


#using dictionary comprehension

numbers1 = [1,2,3,4,5]

squre_numbers1 = {number:number**2 for number in numbers1}

print(squre_numbers1)


#Dictionary Comprehension With Condition
squre_numbers2 = {number:number**2 for number in numbers1 if number>2}

print(squre_numbers2)



