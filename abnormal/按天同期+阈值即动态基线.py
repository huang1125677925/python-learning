import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open('request-number-data1.txt', 'r') as f:
    a = f.readlines()[0]
    d = eval(a)

print(list(d))
data = pd.DataFrame(list(d), columns=['timestamp', 'value'])
print(data)


def f(x):
    return float(x)


data['value'] = data['value'].apply(f)
print(type(data['timestamp'][0]))

print(data['timestamp'].max() - data['timestamp'].min())





class Handle(object):
    mongodb = server_config.SERVER_DIC.get('mongodb')
    
    def __init__(self):
        self.algo = {}
        self.myclient = pymongo.MongoClient(self.mongodb['ip_port'], maxPoolSize=self.mongodb['maxpoolsize'],
                                            connect=False)
        self.logger = log_helper.get_logger()
        self.static = statistic.Statistic()
        self.four_per = fourpecent.FourPercent()
        self.isolation = isolation_forest.IForest()
        self.svm = oneclass_svm.SVM()
        self.ewma = ewma_and_polynomial.EwmaAndPolynomialInterpolation()
        self.algo['a'] = self.isolation
        self.algo['b'] = self.svm
        self.algo['c'] = self.ewma

    

    def threshold_value(self,X, index=3):
        min_value = np.mean(X) - index * np.std(X)
        max_value = np.mean(X) + index * np.std(X)
    
        return min_value, max_value

    
    
    def timestamo_convert_date(self, timestamp):
        
        # 转换成localtime
        time_local = time.localtime(timestamp)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        
        return dt

    def check_update_threshold(self, timestamp):
    
        # 转换成localtime
        time_local = time.localtime(timestamp)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        dt = int(time.strftime("%M", time_local))
        
        if dt%10==0:
            return True
        else:
            return False
    
    # 日期转变为时间戳
    def date_convert(self, date):
        timeArray = time.strptime(date, "%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(timeArray)
        
        return int(timestamp)
    
    def read_mongodb(self, itemid, timeup, timedown,data_mongo):
        
        mydb = self.myclient[self.mongodb['db']]
        mycol = mydb[self.mongodb['collection']]
        timeup = self.timestamo_convert_date(timeup)
        timedown = self.timestamo_convert_date(timedown)
        itemid = int(itemid)
        myquery = {"itemId": itemid, "recordTime": {'$gte': timeup, '$lt': timedown}}
        try:
            query_data = mycol.find(myquery, {"recordTime": 1, "value": 1}).sort('recordTime')
        except:
            self.logger.info('mongodb connect faile,no data is got')
        
        for x in query_data:
            data_mongo.append(float(x.get('value')))

    def data_prepare(self,start_date, end_date,id):
        
        data_mongo = []
        for i in range(1, 7):
            start_date = start_date - 1200
            end_date = end_date - 1200
            start=self.timestamo_convert_date(start_date)
            end=self.timestamo_convert_date(end_date)
            
            self.read_mongodb(id,start,end,data_mongo)
            
        return data_mongo
    
    
    
    def facebook_detect(self, pipe):
        threshold= {}
        _out_pipe, _in_pipe = pipe
        _in_pipe.close()
        
        while True:
            try:
                msg = _out_pipe.recv()
            except EOFError:
                break
            item_id, date_time, value= msg['itemId'], msg['recordTime'], msg['value']
            if self.check_update_threshold(date_time):
                start_time=self.date_convert(date_time)
                end_time=start_time+600
                data_mongo=self.data_prepare(start_time,end_time)
                min_value, max_value = self.threshold_value(data_mongo)
                threshold[item_id]=[min_value,max_value]
                
            if item_id in threshold:
                if value<threshold[item_id][0] or value > threshold[item_id][1]:
                    msg['ruleId']=
                    kafka_helper.KafkaHelper.send_data(msg)
                    self.logger.info('abnoraml {0}---{1}----{2}'.format(item_id,date_time,value))
                else:
    
                    self.logger.info('noraml {0}---{1}----{2}'.format(item_id, date_time, value))
            else:
                self.logger.info('no threshold value {0}---{1}----{2}'.format(item_id, date_time, value))
            
            
            
            
            


if __name__ == "__main__":
    timestamp=1459175064
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = time.strftime("%M", time_local)

    