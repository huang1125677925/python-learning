# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.metrics import mean_squared_error

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from time_predict import read_data1
import pandas as pd
data_read=read_data1.ReadData()

data=data_read.read_data(1673,'2019-07-25 12:00:00','2019-09-23 00:00:00')

data.index = pd.DatetimeIndex(data['timestamp'])
data['value'] = data['value'].astype('float64')
data = data.resample('1800S').mean()

data['value']=data['value'].interpolate(method='time')


print(data.head())
print(data.shape)
all_data = list(data['value'])

dd = np.array(all_data).reshape(-1, 1)
scaler = MinMaxScaler()
scaler.fit(dd)
dd = scaler.transform(dd)
all_data = dd.reshape(1, -1)[0]

trainx = []
trainy = []
train_l=480
test_l=144
for i in range(train_l+test_l, len(all_data)):
    trainx.append(all_data[i - train_l-test_l:i - test_l])
    trainy.append(all_data[i - test_l:i])
print(len(trainx), len(trainy))
print(trainy)
print(trainx)
trainx = np.array(trainx).reshape(-1, train_l, 1)
trainy = np.array(trainy)

index = int(len(trainx) * 0.75)

testx = np.array(trainx[index:])
testy = np.array(trainy[index:])
trainx = np.array(trainx[:index])
trainy = np.array(trainy[:index])

print('trainx.shape = ', trainx.shape)
print('testx.shape = ', testx.shape)
print('trainy.shape = ', trainy.shape)
print('testy.shape = ', testy.shape)

model = Sequential()
model.add(LSTM(100, input_shape=(train_l, 1)))
model.add(Dense(144))
model.compile(optimizer='adam', loss='mse')
model.fit(trainx, trainy, batch_size=2, epochs=2, verbose=1)

res = model.predict(testx)

loss = np.sqrt(np.mean(np.power((res.reshape(-1, 1) - testy.reshape(-1, 1)), 2)))
testx = testx.reshape(-1, train_l)
plot_raw = []
for x in testx[:-1]:
    plot_raw.append(x[0])
plot_raw.extend(testx[-1])

plot_raw = np.array(plot_raw).reshape(-1, 1)
plot_raw = scaler.inverse_transform(plot_raw)
plot_raw = plot_raw.reshape(1, -1)[0]

plot_pred = []
for x in res[::test_l]:
    plot_pred.extend(x)

plot_pred = np.array(plot_pred).reshape(-1, 1)
plot_pred = scaler.inverse_transform(plot_pred)
plot_pred = plot_pred.reshape(1, -1)[0]

plt.figure(figsize=(8, 5))
plt.title('  loss:' + str(loss))
plt.plot(list(range(len(plot_raw))), plot_raw)
plt.plot(list(range(train_l, len(plot_pred) + train_l)), plot_pred)
plt.show()