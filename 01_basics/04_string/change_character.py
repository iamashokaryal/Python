# In this example, we will replace the first character of the string with another character.
# strings are immutable; we cannot change the characters of a string.
#Let's see how we can solve this.



text = 'Hello'

new_text = "J" + text[1:]

print(new_text)


# We cannot do this in string, but we can do this in list
# text = 'Hello'
# text[0] = "J"