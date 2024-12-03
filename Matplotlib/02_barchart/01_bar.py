import matplotlib.pyplot as plt
import pandas as pd

fig,ax = plt.subplots(2,1)


climate_change = pd.read_csv("Matplotlib/src/csv/climate_change.csv", index_col = 0)

# set x label and rotate labels by 90 degree
ax.set_xticklabels(climate_change.index,rotation = 90)

# set y lables as CO2
ax.set_ylabel("Relative Temp")

ax.bar(climate_change.index , climate_change["relative_temp"])

plt.show()