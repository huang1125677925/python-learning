from time_predict.read_data import ReadData
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
read_data=ReadData()

a=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

start=time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S"))-367440+700
end=time.mktime(time.strptime(a, "%Y-%m-%d %H:%M:%S"))-600-367440+700

def convert(end):
    time_local = time.localtime(end)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    
    return dt
def data_prepare(start,end,id):
    check_data=[]
    
    start_date = convert(start )
    end_date = convert((end ))
    
    data = read_data.read_data(id, end_date, start_date)
    
    check_data.extend(list(data['value']))
    
    print('----------------')
    
    
    data_mongo=[]
    for i in range(1,7):
        start_date=convert(start-i*86400)
        end_date=convert((end-i*86400))
    
        data=read_data.read_data(id,end_date,start_date)
    
        print(data)
        print(data.shape)
        data_mongo.extend(list(data['value']))
        
        print('----------------')
    
    return data_mongo,check_data
    


def predict(X,index=3):
    """
    Predict if a particular sample is an outlier or not.

    :param X: the time series to detect of
    :param type X: pandas.Series
    :return: 1 denotes normal, 0 denotes abnormal

    """
    if abs(X[-1] - np.mean(X[:-1])) > index * np.std(X[:-1]):
        return 0
    min_value=np.mean(X)-index * np.std(X)
    max_value=np.mean(X)+index * np.std(X)
    
    return min_value,max_value

def main(id):
    data_history,data_check=data_prepare(start,end,id)
    min_v,max_v=predict(data_history)
    print(a)
    print(data_check)
    for i in data_check:
        if i<min_v or i>max_v:
            print(i)
        else:
            print('not abnormal')
        

