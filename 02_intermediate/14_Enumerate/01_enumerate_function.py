#syntax: enumerate(iterable,start=0)
# iterable = any object that supports iteration
# Start = The index value from which the counter is to be started by default it is 0
lst = ['eat','sleep','work']
string = "Python"

print(list(enumerate(string,2)))

print(list(enumerate(lst)))
