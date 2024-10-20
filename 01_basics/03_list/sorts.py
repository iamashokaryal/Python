#The list's sort() method sorts the elements of a list.

#sort() Syntax : numbers.sort(reverse, key)
#The sort() method can take two optional keyword arguments:

#reverse - By default False. If True is passed, the list is sorted in descending order.
#key - Comparion is based on this function.

numbers = [1,7,3,5,9,2,5]

numbers.sort()

print(numbers)

cities = ['ktm', 'pkr', 'npj','surkhet']

cities.sort()
print(cities)

cities.sort(reverse = True)

print(cities)