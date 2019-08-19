import pymongo
import pandas as pd


class ReadData(object):
    myclient = pymongo.MongoClient('10.1.11.14:27017')
    mydb = myclient["aiops"]
    mycol = mydb["item"]
    
    def read_data(self, id, timeup='2019-07-29 05:00:00', timedown='2019-07-29 10:00:00'):
        timeleft = '2019-08-' + timeup
        timeright = '2019-08-' + timedown
        myquery = {"itemId": id, "recordTime": {'$gte': timeleft, '$lte': timeright}}
        query_data1 = self.mycol.find(myquery, {'recordTime': 1, "value": 1}).sort('recordTime')
        
        data = []
        for x in query_data1:
            temp = []
            temp.append(x.get('recordTime'))
            temp.append(float(x.get('value')))
            data.append(temp)
        
        d = pd.DataFrame(data, columns=['timedata', 'value'])
        
        return d