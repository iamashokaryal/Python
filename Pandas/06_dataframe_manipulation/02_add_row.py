import pandas as pd

data = {
    'Name':['Ram','Shyam','Hari'],
    'Age':[22,25,28],
    'Address':['Ktm','Btl','Pkr']

}

df = pd.DataFrame(data)
print('Original dataframe: \n', df)


hobby = ['Singing','Dancing', 'Coding']
df.loc[len(df.index)]= ['ash',22,'Jhapa']

print('Modified array is : \n',df)
# df['Hobby'] = hobby

# print(df.loc[2])