import matplotlib.pyplot as plt
import pymongo
import pandas as pd
import statsmodels.api as sm


myclient = pymongo.MongoClient('10.1.11.14:27017')
mydb = myclient["aiops"]
mycol = mydb["item"]

itemid = []
query_id = mycol.distinct('itemId')
for item in query_id:
    itemid.append(int(item))
print('指标id采集完成')
i = 0
temp = []
for id in itemid:
    i = i + 1
    myquery = {"itemId": id, "recordTime": {'$gte': '2019-07-28 05:00:00', '$lt': '2019-07-28 13:00:00'}}
    query_data1 = mycol.find(myquery, {"value": 1})
    
    data = []
    for x in query_data1:
        data.append(float(x.get('value')))
    print('数据采集完成--{}'.format(id))
    
    if len(data) < 10:
        print('数据太少--{}'.format(id))
        print(data)
        continue
    
    a = list(sm.tsa.stattools.adfuller(data))
    d = min(a[4].values())
    y = 0
    if pd.isna(a[0]):
        y = 2
    elif a[0] < d:
        y = 1
    t = [id, y]
    temp.append(t)
    print(t)
    print('{}的图片画图完毕'.format(id))
pd.DataFrame(data=temp, columns=['id', 'value']).to_csv('itemid_stationary.csv')
