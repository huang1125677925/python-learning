import pymongo
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from time_predict import read_data1
import numpy as np


class ReadData(object):
    myclient = pymongo.MongoClient('10.1.11.14:27017',username='aiops', password='aiops')
    mydb = myclient["aiops"]
    mycol = mydb["item"]
    
    def read_data(self, id, timeup='2019-07-29 05:00:00', timedown='2019-07-29 10:00:00'):

        myquery = {"itemId": id, "recordTime": {'$gte': timeup, '$lte': timedown}}
        query_data1 = self.mycol.find(myquery, {'recordTime': 1, "value": 1}).sort([('recordTime', pymongo.ASCENDING),]).limit(1)
        query_data2=self.mycol.find(myquery, {'recordTime': 1, "value": 1}).sort([
                    ('recordTime', pymongo.DESCENDING)]).limit(1)
        data = []
        for x in query_data1:
            if x.get('value')=='null':
                continue
            else:
                temp = []
                temp.append(x.get('recordTime'))
                data.append(temp)
        
        for x in query_data2:
            if x.get('value')=='null':
                continue
            else:
                temp = []
                temp.append(x.get('recordTime'))
                data.append(temp)

        
        if len(data)==2:
            d1 = datetime.datetime.strptime(data[1][0], '%Y-%m-%d %H:%M:%S')
            d2 = datetime.datetime.strptime(data[0][0], '%Y-%m-%d %H:%M:%S')
            delta = d1 - d2
            data.append(delta.days)
            return data
        else:
            return []

    def read_data_event(self, id, timeup='2019-07-29 05:00:00', timedown='2019-09-29 10:00:00'):
        myquery = {"itemId": id, "recordTime": {'$gte': timeup, '$lte': timedown}}
        query_data1 = self.mycol.find(myquery)
    
        
        
        return query_data1.count(),query_data1[0]
    def read_itemid(self):
        
        query_data1 = self.mycol.distinct('itemId')
    
        data = []
        for x in query_data1:
            
            data.append(x)
    
        

        return data
if __name__ == '__main__':
    
    ddd=ReadData()
    # itemid=d.read_itemid()
    # print(len(itemid))
    # timeup='2019-08-01 00:00:00'
    # timedown='2019-09-16 00:00:00'
    # min_id=0
    # min_date='2019-09-16 00:00:00'
    # res=[]
    # for x in itemid:
    #     if x!=None:
    #         data=d.read_data(x,timeup,timedown)
    #         # if data>100:
    #         if data :
    #             data.append(x)
    #             print(data)
    #             res.append(data)
    #
    #
    # data=pd.DataFrame(data=res,columns=['start','end','day','id'])
    #
    #
    # print(data['day'].max())
    #
    # data.to_csv('item_id_num_statis.csv')
    
    data=pd.read_csv('item_id_num_statis.csv')
    item_id_great_20=data[data['day']==15]
    data_read = read_data1.ReadData()
    
    for id,day in zip(list(item_id_great_20['id']),list(item_id_great_20['day'])):
        count,l=ddd.read_data_event(id)
        step=l['step']
        print(id,day,count,step,count//(86400//step))

        d = data_read.read_data(id, '2019-07-25 12:00:00', '2019-09-20 15:00:00')
        
        # print(data.shape)
        d.dropna(axis=1)
        d['value'] = list(map(float, d['value']))
        dd=np.array(d['value'])
        if np.mean(dd)==np.min(dd):
            continue
        plt.title('id is {0} day is {1}'.format(id,day))
        d['value'].plot()
        plt.show()
    
    

    
            
            
            
    
    