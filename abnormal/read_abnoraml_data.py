import pymongo
import pandas as pd
import matplotlib.pyplot as plt


class ReadData(object):
    myclient = pymongo.MongoClient('10.1.11.14:27017')
    mydb = myclient["aiops"]
    mycol = mydb["event"]
    
    def read_data(self, id, timeup='2019-07-29 05:00:00', timedown='2019-07-29 10:00:00'):
        timeleft = '2019-08-' + timeup
        timeright = '2019-08-' + timedown
        myquery = {"itemId": id, "recordTime": {'$gte': timeleft, '$lte': timeright}}
        query_data1 = self.mycol.find(myquery, {'recordTime': 1, "value": 1}).sort('recordTime')
        
        data = []
        for x in query_data1:
            if x.get('value')=='null':
                continue
            else:
                temp = []
                temp.append(x.get('recordTime'))
                temp.append(float(x.get('value')))
                data.append(temp)
        
        d = pd.DataFrame(data, columns=['timedata', 'value'])
        
        return d

    def read_data_event(self, id, timeup='2019-07-29 05:00:00', timedown='2019-07-29 10:00:00'):
        timeleft = '2019-08-' + timeup
        timeright = '2019-08-' + timedown
        myquery = {"itemId": id, "recordTime": {'$gte': timeleft, '$lte': timeright}}
        query_data1 = self.mycol.find(myquery)
    
        
    
        return query_data1.count()
    def read_itemid(self):
        
        query_data1 = self.mycol.distinct('itemId')
    
        data = []
        for x in query_data1:
            
            data.append(x)
    
        

        return data
    
d=ReadData()
itemid=d.read_itemid()
event_stat=[]
for x in itemid:
    if x!=None:
        data=d.read_data_event(x,'17 00:00:00','21 00:00:00')
        if data>100:
            print(x)
        event_stat.append([x,data])
        

event_item=pd.DataFrame(event_stat,columns=['id','event_num'])

print(event_item.describe())