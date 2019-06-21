
df.columns = ['ds', 'y']

df['ds'] = pd.to_datetime(df['ds'], unit='s')

df.shape

traindata = df.loc[:1900, :]
testdata = df.loc[1901:, :]
print(traindata.shape, testdata.shape)

import numpy as np


def normalize_time_series_by_max_min(data):
	max_value = np.max(data)
	min_value = np.min(data)
	normalized_time_series = [0.0] * len(data)
	if max_value - min_value > 0:
		normalized_time_series = list((np.array(data) - min_value) / float(max_value - min_value))

	return normalized_time_series


from sklearn.metrics import mean_squared_error
from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()

errorlist = []
for i in range(2, 60):
	temp = list(range(1901))[::i]
	if 1901 not in temp:
		temp.append(1901)
	train = traindata.loc[temp, :]
	train.reset_index()
	m = Prophet()
	m.fit(train)
	future = m.make_future_dataframe(periods=100, freq='5T', include_history=False)
	forecast = m.predict(future)
	forecast = list(forecast['yhat'])
	forecast = normalize_time_series_by_max_min(forecast)
	realdata = normalize_time_series_by_max_min(list(testdata['y']))

	error = mean_squared_error(forecast, realdata)
	print('间隔为{0}的误差为{1}'.format(i, error))
	errorlist.append(error)
import matplotlib.pyplot as plt

plt.plot(errorlist)
plt.ylabel('error')
plt.show()