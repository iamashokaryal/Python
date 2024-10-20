
numbers = [1,2,3,4,5,6,7,8]

mixed_list = [1,2,3,'hello',6,8,'Python']

#for slicing we use new_list = old_list_name[start:end]
#here start is inclusive and end is exlclusive. means start chai list mai aauxa tara end chai list maa pardaina

new_numbers = numbers[2:5]
print(new_numbers)   #here statrt = 2 (inclusive) and end = 5 ko value parena because it is exclusive

new_mixed_list = mixed_list[3:-1]

print(new_mixed_list)


#It's possible to omit the start and end index in slicing.
# Omit Start Index: If we omit the start index, the slicing starts from the first item (not the first index).

print(numbers[:4])

# Omit End Index :If we omit the end index, the slicing ends at the last item (not the last index).

print(numbers[2:])

#skip both start and end index

print(numbers[:])
