# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in

import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.metrics import mean_squared_error

from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, CuDNNLSTM, CuDNNGRU
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os

for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        path = os.path.join(dirname, filename)
        print(path)
        data = pd.read_csv(path)
        data = data.loc[:, 'value']
        all_data = list(map(float, list(data)))


        dd =np.array(all_data).reshape(-1,1)
        scaler = MinMaxScaler()
        scaler.fit(dd)
        dd = scaler.transform(dd)
        all_data=dd.reshape(1, -1)[0]
        
        trainx = []
        trainy = []
        for i in range(190, len(all_data)):
            trainx.append(all_data[i - 190:i - 10])
            trainy.append(all_data[i - 10:i])
        print(len(trainx), len(trainy))
        
        trainx = np.array(trainx).reshape(-1, 180, 1)
        trainy = np.array(trainy)
        
        index = int(len(all_data) * 0.75)
        
        testx = np.array(trainx[index:])
        testy = np.array(trainy[index:])
        trainx = np.array(trainx[:index])
        trainy = np.array(trainy[:index])
        
        print('trainx.shape = ', trainx.shape)
        print('testx.shape = ', testx.shape)
        print('trainy.shape = ', trainy.shape)
        print('testy.shape = ', testy.shape)
        
        model = Sequential()
        model.add(CuDNNLSTM(100, input_shape=(180, 1)))
        model.add(Dense(10))
        model.compile(optimizer='adam', loss='mse')
        model.fit(trainx, trainy, batch_size=1, epochs=2, verbose=1)
        
        
        
        res = model.predict(testx)
        model.evaluate(res,testy)
        
        testx = testx.reshape(-1, 180)
        plot_raw = []
        for x in testx[:-1]:
            plot_raw.append(x[0])
        plot_raw.extend(testx[-1])
        
        plot_raw=np.array(plot_raw).reshape(-1,1)
        plot_raw=scaler.inverse_transform(plot_raw)
        plot_raw=plot_raw.reshape(1,-1)[0]
        
        
        plot_pred = []
        for x in res[::10]:
            plot_pred.extend(x)
        
        plot_pred=np.array(plot_pred).reshape(-1,1)
        plot_pred = scaler.inverse_transform(plot_pred)
        plot_pred=plot_pred.reshape(1,-1)[0]
        
        plt.title(path)
        plt.figure(figsize=(10,8))
        plt.plot(list(range(len(plot_raw))), plot_raw)
        plt.plot(list(range(180, len(plot_pred) + 180)), plot_pred)
        plt.show()

