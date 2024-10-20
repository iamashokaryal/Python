def compute_table(n):

    for count in range (1,21):
        total = count * n 
        print(n,'*',count,'=',total)

a = int(input("enter the number:"))
compute_table(a)
