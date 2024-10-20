def thousand_separator(number):

    number = str(number)

    number = number[::-1]

    separated = ''

    for i in range(0,len(number)):
        if i%3==0 and i!=0:
            separated +=','
    
        separated += number[i]
    
    separated = separated[::-1]
    return separated
  
sep = thousand_separator(1000000)     

print(sep)