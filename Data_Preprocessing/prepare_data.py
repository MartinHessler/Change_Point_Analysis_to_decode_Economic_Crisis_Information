import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

financial_data = pd.read_csv('Financial_Time_Series_Centered_Interval__42days.csv', 
							index_col = 'Centre_of_Interval', 
							usecols = ['Centre_of_Interval', 'Mean_Correlation'])
print(financial_data)
print(financial_data.shape)

thinning_by = 40

thinned_financial_data = financial_data.loc[::thinning_by]
print(financial_data.shape)
print(thinned_financial_data.shape)
fig, ax = plt.subplots(1,1)
ax.xaxis.set_major_locator(mdates.YearLocator(base=1, month=6, day=30, tz=None))
plt.plot(financial_data)
plt.plot(thinned_financial_data)
plt.show()

np_array_thinned_data = np.squeeze(np.array(thinned_financial_data.loc['1992-01-31':]))
print(np_array_thinned_data.shape)
np_array_thinned_time = np.arange(0,np_array_thinned_data.size,1)
print(np_array_thinned_time.shape)
print(np_array_thinned_time)
plt.plot(np_array_thinned_time, np_array_thinned_data)
plt.show()

np.save('thinnedFinancialData' + str(thinning_by) + '.npy', np_array_thinned_data)
np.save('thinned_time_thinning' + str(thinning_by) + '.npy', np_array_thinned_time)


