import matplotlib.pyplot as plt
import pandas as pd

fig,ax = plt.subplots(2,1)

climate_change = pd.read_csv("Matplotlib/src/csv/climate_change.csv", index_col = 0)

# set x label and rotate labels by 90 degree
ax[0].set_xticklabels(climate_change.index,rotation = 90)

# set y lables as Relative Temp
ax[0].set_ylabel("Relative Temp")

ax[0].bar(climate_change.index , climate_change["relative_temp"])

ax[1].set_xticklabels(climate_change.index,rotation = 90)

ax[1].set_ylabel("Co2")

ax[1].bar(climate_change.index , climate_change["co2"])


plt.show()