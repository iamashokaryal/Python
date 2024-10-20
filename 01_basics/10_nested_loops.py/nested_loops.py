
#It's possible to put a loop inside another loop. This is known as a nested loop.

#In a nested loop, the inner loop is executed for each iteration of the outer loop.


attributes = ['Electric', 'Fast']
cars = ['Tesla', 'Mercedes']

for att in attributes:
    for ca in cars:
        print(att,ca)