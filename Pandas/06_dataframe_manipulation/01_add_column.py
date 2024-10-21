import pandas as pd

data = {
    'Name':['Ram','Shyam','Hari'],
    'Age':[22,25,28],
    'Address':['Ktm','Btl','Pkr']

}

df = pd.DataFrame(data)

hobby = ['Singing','Dancing', 'Coding']

df['Hobby'] = hobby

print(df)