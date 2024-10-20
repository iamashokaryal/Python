#There are two things we need to remember while writing to a file.
#If we try to open a file that doesn't exist, a new file is created.
#If a file already exists, its content is erased, and new content is added to the file.

with open('a.txt','w') as f:
    f.write('Python is awesome \n')
    f.write('Hello Pthon')

    #file maa arko palta write garda pahila ko erase hunxa

    # pahilai lekheko file maa jodna hamile append argument use garxam
    

with open('a.txt','w')as f:
    f.write('i love python only')
    
