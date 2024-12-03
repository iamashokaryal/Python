import matplotlib.pyplot as plt
import pandas as pd

arr1 = pd.array([1,2,3,4,5,6,7])

arr2 = pd.array([2,4,6,8,10,12,14])

plt.plot(arr1,arr2,color='blue',linestyle = "--",marker = 'o')

plt.xlabel("x axis.")

plt.ylabel("Y axis.")

plt.title("MY DATA")

plt.show()

