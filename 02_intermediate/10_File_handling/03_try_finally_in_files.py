
try:
    f = open('a.txt', 'r')

    content = f.read()

    print(content)

finally:
    f.close()

    #There is a better way to write this above code using the with...open syntax.
    #  Here's how:

    with open('a.txt','r') as f:
        content = f.read()
        print(content)

#Remember : Make a habit of using with..open syntax when working with files so that you don't have to worry about closing the file.
