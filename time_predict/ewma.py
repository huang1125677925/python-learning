from time_predict import read_data
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame
from datetime import datetime
import numpy as np

data_read=read_data.ReadData()

data=data_read.read_data(1638,'12 12:00:00','12 18:00:00')


datels = [datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in data['timedata']]

data['timedata']=datels
index=pd.DatetimeIndex(start=data['timedata'].min(),end=data['timedata'].max(),freq='T')
data1=DataFrame([None]*len(index),columns=['value'])
data1['timedata']=index


merge_data=data1.merge(data,left_on='timedata',right_on='timedata',how='left')

data_mean=np.mean(merge_data.loc[merge_data['value_y'].notna(),'value_y'])

merge_data.loc[merge_data['value_y'].isna(),'value_y']=data_mean



merge_data.drop('value_x',axis=1,inplace=True)
l=len(merge_data['value_y'])
plt.plot(list(range(l)),merge_data['value_y'])

print(merge_data)

plt.plot(list(range(l)),merge_data['value_y'].ewm(span=5,adjust=True).mean(),color='r')
# plt.plot(list(range(l)),merge_data['value_y'].ewm(span=5,adjust=True).var(),color='b')
plt.show()


print(merge_data['value_y'].rolling(3).mean())

print(merge_data.ewma(span=2).mean())