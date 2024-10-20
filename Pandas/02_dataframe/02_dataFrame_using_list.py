import pandas as pd

data = [['John',10,'KTM'],
        ['Hari',22,'NPJ'],
        ['Shyam',26,'Dang']]

df = pd.DataFrame(data, columns=['Name','Age','City'])

print(df)