#The get() method returns the value of the specified key. If the key doesn't exist, instead of getting an error, 
# we get None, which means no value.

scores = {'Physics': 67, "Math": 90}

print(scores.get('Physics'))
print(scores.get('Math'))