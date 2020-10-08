from time_predict import read_data1
import pandas as pd
data_read=read_data1.ReadData()

data=data_read.read_data(1492,'2019-07-25 12:00:00','2019-09-23 00:00:00')

data.index = pd.DatetimeIndex(data['timestamp'])
data['value'] = data['value'].astype('float64')
data = data.resample('1800S').mean()

print(data.head())