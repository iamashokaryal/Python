def check_pal(text):

    if text == '' or len(text)==1:
        return 'Wow! it is a Palindrome.'

    elif text[0]==text[-1]:
        return check_pal(text[1:-1])

    else:
        return 'oops!, it is Not a Palindrome.'

text = input("Enter the letter you want to check: \n").lower()

result = check_pal(text)

print(result)