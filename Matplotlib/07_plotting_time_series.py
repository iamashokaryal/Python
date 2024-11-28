from matplotlib import pyplot as plt
import pandas as pd

climate_change = pd.read_csv("Matplotlib/src/csv/climate_change.csv", parse_dates=["date"], index_col="date")
DatetimeIndex = ['1958-03-06', '1958-04-06','1958-05-06',
'1958-06-06'
,
'1958-07-06'
,
'1958-08-06'
,
'1958-09-06'
,
'1958-10-06'
,
'1958-11-06'
,
'1958-12-06'
,
'2016-03-06'
]

plt.plot(DatetimeIndex,climate_change["co2"])

plt.show()
