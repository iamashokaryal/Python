
#1.convert string to tuple

string = 'Ashok'
result = tuple(string)

print(result)

#2.convert tuple to tuple

list_sample = [1,2,3,4]
result1 = tuple(list_sample)
print(result1)

#3.convert dictionary to tuple

dict_sample = {
    'name':'ashok',
    'address': 'Arghakhanchi'
}
result2 = tuple(dict_sample)

print(result2)

#4.convert set to tuple

set_sample = {1,2,3,4,'hello'}

result3 = tuple(set_sample)

print(result3)
