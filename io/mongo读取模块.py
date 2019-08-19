
import itertools
import pymongo
import numpy as np
import time
SERVER_DIC = {
    'kafka': {
        'bootstrap_servers':'10.1.11.16:9093,10.1.11.31:9093,10.1.11.115:9093',
        'group': 'inline',
        'std_topic': 'std-item',
        'alarm_topic': 'alarm-data',
        'auto_offset_reset': 'latest'  # latest or earliest
    },
    'mongodb':{
        'ip_port':'10.1.11.14:27017',
        'db':'aiops',
        'collection':'event',
        'maxpoolsize':3

    },
    'mongodb_item':{
        'ip_port':'10.1.11.14:27017',
        'db':'aiops',
        'collection':'item',
        'maxpoolsize':3

    }
    
}


class Handle(object):
    mongodb = SERVER_DIC.get('mongodb')
    mongodb_item=SERVER_DIC.get('mongodb_item')
    def __init__(self):
        self.myclient = pymongo.MongoClient(self.mongodb['ip_port'], maxPoolSize=self.mongodb['maxpoolsize'],
                                            connect=False)
        self.myclient_item=pymongo.MongoClient(self.mongodb_item['ip_port'], maxPoolSize=self.mongodb_item['maxpoolsize'],
                                            connect=False)
    def timestamo_convert_date(self, timestamp):
        
        # 转换成localtime
        time_local = time.localtime(timestamp)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        
        return dt
    
    # 日期转变为时间戳
    def date_convert(self, date):
        timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(timeArray)
        
        return int(timestamp)
    
    def read_mongodb_perid_abnormal(self,timeup, timedown,id):
        
        mydb = self.myclient[self.mongodb['db']]
        mycol = mydb[self.mongodb['collection']]
        timeup = self.timestamo_convert_date(timeup)
        timedown = self.timestamo_convert_date(timedown)
        
        myquery = { 'itemId':id,"recordTime": {'$gte': timeup, '$lt': timedown}}
        try:
            query_data = mycol.find(myquery, {"recordTime": 1, "value": 1})
        except:
            print('读取失败')
        
        return query_data.count()
    
    
    def read_mongo_item_data(self,timeup, timedown,id):
        mydb = self.myclient_item[self.mongodb_item['db']]
        mycol = mydb[self.mongodb_item['collection']]
        timeup = self.timestamo_convert_date(timeup)
        timedown = self.timestamo_convert_date(timedown)
    
        myquery = {'itemId':id,"recordTime": {'$gte': timeup, '$lt': timedown}}
        try:
            query_data = mycol.find(myquery, {"recordTime": 1, "value": 1})
        except:
            print('读取失败')
            
        data=[]
        for x in query_data:
            data.append(float(x.get('value')))
        
        
    
        return data

    def read_mongodb_all_abnormal(self, timeup, timedown):
    
        mydb = self.myclient[self.mongodb['db']]
        mycol = mydb[self.mongodb['collection']]
        timeup = self.timestamo_convert_date(timeup)
        timedown = self.timestamo_convert_date(timedown)
    
        myquery = {"recordTime": {'$gte': timeup, '$lt': timedown}}
        try:
            query_data = mycol.find(myquery, {"recordTime": 1, "value": 1})
        except:
            print('读取失败')
    
        return query_data.count()

    def read_mongodb_event_id(self, timeup, timedown):
    
        mydb = self.myclient[self.mongodb['db']]
        mycol = mydb[self.mongodb['collection']]
        timeup = self.timestamo_convert_date(timeup)
        timedown = self.timestamo_convert_date(timedown)
    
        
        try:
            query_data = mycol.distinct('itemId')
        except:
            print('读取失败')
    
        temp=[]
        for item in query_data:
            temp.append(item)
        
        return temp


def find_max_abnormal_count():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    tim = '2019-08-06 00:00:00'
    tim1 = '2019-08-08 14:00:00'
    a = Handle()
    start = a.date_convert(tim)
    start1 = start + 3600
    end = a.date_convert(tim1)
    
    itemid = a.read_mongodb_event_id(start, end)
    xlist = []
    ylist = []
    for id in itemid:
        
        if id:
            xlist.append(id)
            r = a.read_mongodb(start, end, id)
            ylist.append(r)
    
    mean = np.mean(ylist)
    
    for i in range(len(ylist)):
        if ylist[i] > mean:
            print(xlist[i])



def plot_abnoraml_count():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    tim = '2019-08-08 00:00:00'
    tim1 = '2019-08-09 09:00:00'
    a = Handle()
    start = a.date_convert(tim)
    start1 = start + 3600
    end = a.date_convert(tim1)
    
    temp=[]
    while start1<=end:
        temp.append(a.read_mongodb_all_abnormal(start,start1))
        start,start1=start1,start1+3600

    xticks = pd.date_range(start=tim, end=tim1,
                           freq='H')
    print(xticks)
    plt.plot(list(range(len(temp))), temp)
    plt.title('2019-08-08 Abnormal Number Per Hour')
    plt.xticks(list(range(len(temp))), xticks.strftime("%Y-%m-%d %H-%M"), rotation=45)
    
    
    plt.show()
    
import numpy as np


class Statistic(object):


    def __init__(self, index=3):
        """
        :param index: multiple of standard deviation
        :param type: int or float
        """
        self.index = index

    def predict(self, X):
        """
        Predict if a particular sample is an outlier or not.

        :param X: the time series to detect of
        :param type X: pandas.Series
        :return: 1 denotes normal, 0 denotes abnormal

        """
        if abs(X[-1] - np.mean(X[:-1])) > self.index * np.std(X[:-1]):
            return 0
        return 1

def check_data_abnoraml(data):
    x=[]
    y=[]
    a=Statistic()
    for i in range(180,len(data)):
        if a.predict(data[i-180:i])==0:
            x.append(i)
            y.append(data[i])
            
    
    return x,y


def scaler_raw_data_and_plot_thedata_and_abnoraml():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler, StandardScaler, Normalizer, RobustScaler
    
    tim = '2019-08-09 00:00:00'
    tim1 = '2019-08-09 14:00:00'
    a = Handle()
    start = a.date_convert(tim)
    end = a.date_convert(tim1)
    
    raw_data = a.read_mongo_item_data(start, end, 9486)
    
    dd = np.array(raw_data).reshape(-1, 1)
    
    print(dd)
    scaler = MinMaxScaler()
    scaler.fit(dd)
    min_max_data = scaler.transform(dd)
    min_max_data_y = min_max_data.reshape(-1, 1)
    min_max_datax, min_max_datay = check_data_abnoraml(min_max_data_y)
    
    print(min_max_data)
    standard = StandardScaler()
    
    plt.figure(figsize=[20, 10])
    x = list(range(len(raw_data)))
    raw_x, raw_y = check_data_abnoraml(raw_data)
    
    standard.fit(dd)
    standard_data = standard.transform(dd)
    
    robust = RobustScaler()
    robust.fit(dd)
    robust_data = robust.transform(dd)
    
    normal = Normalizer()
    normal.fit(dd)
    normal_data = normal.transform(dd)
    
    plt.subplot(5, 1, 1)
    plt.plot(x, raw_data, '-')
    plt.scatter(raw_x, raw_y, color='r')
    plt.title('contrast rawdata and scaler data ID 1631')
    plt.ylabel('raw data')
    
    plt.subplot(5, 1, 2)
    plt.plot(x, min_max_data_y, '--')
    plt.scatter(min_max_datax, min_max_datay, color='r')
    plt.ylabel('min_max scaler data')
    
    plt.subplot(5, 1, 3)
    plt.plot(x, standard_data.reshape(-1, 1), '--')
    plt.ylabel('standard scaler data')
    
    plt.subplot(5, 1, 4)
    plt.plot(x, robust_data.reshape(-1, 1), '--')
    plt.ylabel('robust scaler data')
    
    plt.subplot(5, 1, 5)
    plt.plot(x, normal_data.reshape(-1, 1), '--')
    plt.ylabel('normal scaler data')
    
    plt.show()

if __name__ == "__main__":

    
    
    
        
        
        
    
    
    
    





















