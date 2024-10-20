
# Write a program to calculate the sum of integers entered by the user.

# Create a variable named total with value 0 at the beginning.
# Create a while loop with condition True.
# If the user enters 0 or negative integer, use break to terminate the loop.
# If the user enters a positive number, add it to the total variable.
# Outside of the loop, print the total.
# Note: The negative number shouldn't be added to the total variable.

total = 0
while True:

    n = int(input())
    if n==0 or n<0:
        break
    total = n+total
# print the total
print(total)