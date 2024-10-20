import pandas as pd

data = [10,20,30]

series = pd.Series(data, index = ['x','y','z'])

print(series)

print(series['x'])