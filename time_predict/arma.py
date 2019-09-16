from time_predict import read_data1
import matplotlib.pyplot as plt
import pandas as pd
from pandas import Series,DataFrame
from datetime import datetime


data_read=read_data1.ReadData()

data=data_read.read_data(1631,'13 12:00:00','13 15:00:00')


datels = [datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in data['timedata']]

data['timedata']=datels
index=pd.DatetimeIndex(start=data['timedata'].min(),end=data['timedata'].max(),freq='T')
data1=DataFrame([None]*len(index),columns=['value'])
data1['timedata']=index


merge_data=data1.merge(data,left_on='timedata',right_on='timedata',how='left')
merge_data.loc[merge_data['value_y'].isna(),'value_y']=90
print(merge_data)

test_data=Series(merge_data['value_y'])
test_data.index=merge_data['timedata']
plt.plot(test_data.values)
plt.show()
from statsmodels.tsa.stattools import adfuller


def test_stationarity(timeseries):
    # Determing rolling statistics
    rolmean = timeseries.rolling(12).mean()
    rolstd = timeseries.rolling(12).std()
    # Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue', label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label='Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show(block=False)

    # Perform Dickey-Fuller test:
    print('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
    for key, value in dftest[4].items():
        dfoutput['Critical Value (%s)' % key] = value
    print(dfoutput)

test_stationarity(test_data)


expwighted_avg = pd.DataFrame.ewm(test_data, halflife=12).mean()
plt.plot(test_data)
plt.plot(expwighted_avg, color='red')
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose
decomposition = seasonal_decompose(test_data)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.subplot(411)
plt.plot(test_data, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal,label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
plt.show()