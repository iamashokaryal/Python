
def find_length(text):
    if text =='':
        return 0

    else:
        return find_length(text[1:])+1

text = input()
result = find_length(text)

print(f"length is {result}")