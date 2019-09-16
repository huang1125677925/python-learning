import pymongo
import pandas as pd

class ReadData(object):
    myclient = pymongo.MongoClient('10.1.11.14:27017', username='aiops', password='aiops')
    mydb = myclient["aiops"]
    mycol = mydb["item"]
    
    def read_data(self,id,timeleft='2019-07-29 05:00:00',timeright='2019-07-29 10:00:00'):
        myquery = {"itemId": id, "recordTime": {'$gte':timeleft , '$lte': timeright}}
        query_data1 = self.mycol.find(myquery, {'recordTime':1,"value": 1}).sort('recordTime')
        
        data = []
        for x in query_data1:
            temp = []
            value = x.get('value')
            if value == 'null':
                continue
            else:
                temp.append(x.get('recordTime'))
                temp.append(value)
            data.append(temp)

        d=pd.DataFrame(data,columns=['timestamp','value'])
        
        return d

    def read_itemid(self):
        query_data1 = self.mycol.distinct('itemId')
    
        data = []
        for x in query_data1:
            data.append(x)
            
        return data

