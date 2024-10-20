#using While loop 

num = n = int(input('Enter number :'))

total = 0
i = 1
while i<=n:

    total = i+total
    i = i+1
print("sum using while loop = ", total )

#using for loop

#num = int(input('Enter number :'))

sum = 0

for i in range (1, num+1):
    sum  = sum +i

print('Sum using for loop =', sum)

