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
data_std=np.std(merge_data.loc[merge_data['value_y'].notna(),'value_y'])
min_field=data_mean-4*data_std
max_field=data_mean+4*data_std

merge_data.loc[merge_data['value_y'].isna(),'value_y']=data_mean

merge_data.loc[merge_data['value_y']>max_field,'value_y']=data_mean

merge_data.loc[merge_data['value_y']<min_field,'value_y']=data_mean



test_data=Series(merge_data['value_y'])
test_data.index=merge_data['timedata']





print("Citi Bike data:\n{}".format(test_data.head()))

import matplotlib.pyplot as plt

import pandas as pd

plt.figure(figsize=(10, 3))
xticks = pd.date_range(start=test_data.index.min(), end=test_data.index.max(),
                       freq='T')
plt.xticks(xticks, xticks.strftime("%"), rotation=90, ha="left")
plt.plot(test_data, linewidth=1)
plt.xlabel("Date")
plt.ylabel("Rentals")
plt.show()

# extract the target values (number of rentals)
import numpy as np
y = test_data.values
# convert the time to POSIX time using "%s"
X = np.array(test_data.index.strftime("%s").astype("int")).reshape(-1, 1)

#encoding=utf-8
# use the first 184 data points for training, and the rest for testing
n_train = 184
    # function to evaluate and plot a regressor on a given feature set
def eval_on_features(features, target, regressor):
    # split the given features into a training and a test set
    X_train, X_test = features[:n_train], features[n_train:]
    # also split the target array
    y_train, y_test = target[:n_train], target[n_train:] 
    regressor.fit(X_train, y_train)
    # print("Test-set R^2: {:.2f}".format(regressor.score(X_test, y_test)))
    y_pred = regressor.predict(X_test)
    y_pred_train = regressor.predict(X_train)
    plt.figure(figsize=(20, 8))
    plt.xticks(range(0, len(X)), xticks.strftime("%a %H-%M"), rotation=90,
               ha="left")
    plt.plot(range(n_train), y_train, label="train")
    plt.plot(range(n_train, len(y_test) + n_train), y_test, color='b', label="test")
    plt.plot(range(n_train), y_pred_train, color='r',label="prediction train")
    plt.plot(range(n_train, len(y_test) + n_train), y_pred, color='r',
             label="prediction test")
    plt.legend(loc=(1.01, 0))
    plt.xlabel("Date")
    plt.ylabel("Rentals")
    plt.title('item ID--{}'.format(id))
    plt.show()


from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor
regressor = RandomForestRegressor(n_estimators=150, random_state=0,max_depth=2)
regressor1=GradientBoostingRegressor(n_estimators=100, learning_rate=0.1,
    max_depth=5, random_state=0, loss='ls')
X_hour = np.array(test_data.index.minute).reshape(-1, 1)
eval_on_features(X_hour, y, regressor)


X_hour_week = np.hstack([np.array(test_data.index.dayofweek).reshape(-1, 1),
                             np.array(test_data.index.minute).reshape(-1, 1)])
eval_on_features(X_hour_week, y, regressor)
