try:
    numerator = int(input('Enter Numerator :'))
    denominator = int(input('Enter Denominator:'))

    result = numerator/denominator

    print(result)


    my_list = [1,2,3]

    index = int(input('Enter index:'))

    print(my_list[index])

except ZeroDivisionError:
    print("Denominator cannot be 0, try again with other value.")

except IndexError:
    print("Index is worng, Enter valid index.")

