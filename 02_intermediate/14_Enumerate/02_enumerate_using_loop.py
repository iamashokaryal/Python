l1 = ["eat", "sleep", "repeat"]

for ele in enumerate(l1):
    print(ele)

for count,ele in enumerate(l1):
    print(count)
    print(ele)

for count,ele in enumerate(l1,100):
    print(count,ele)

