import pandas as pd


data = {
    'Name':['Ashok','Hero'],
    'Age':[22,25],
    'Location':['Arg','Ktm']
}
df = pd.DataFrame(data, index=['A','B'])

print(df['Name']['A'])



