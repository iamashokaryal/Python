n = int(input('enter number :'))

for item in range(1,n+1):

    if item % 2 == 0:
        continue

    print(item)