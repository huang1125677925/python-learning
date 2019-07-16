#!/usr/bin/env python
# coding: utf-8
import pymongo
import pandas as pd
myclient = pymongo.MongoClient('58.16.78.136:27017')
dblist = myclient.list_database_names()
print(dblist)
mydb = myclient["test"]
collist = mydb.list_collection_names()
print(collist)


mycol = mydb["item"]
temp = []
for x in mycol.find({}, { "itemId": 1,"recordTime": 1, "value": 1 }):
    td = x
    temp.append([td.get('itemId'), td.get('recordTime'), td.get('value')])
print(len(temp))
data = pd.DataFrame(temp, columns=['itemId', 'recordTime', 'value'])


item=list((set(list(data['itemId']))))



valuelist=[]
for i in item:
    valuelist.append(data[data['itemId']==i].loc[:,['value']].describe()['value'][2])


# In[69]:


for i in range(len(valuelist)):
    if valuelist[i]=='null':
        valuelist[i]='0'
        


# In[74]:


valuelst=list(map(float,valuelist))
valuelst


# In[105]:


res=[]
for i in range(len(item)):
    if valuelst[i]<=1 or valuelst[i]>10000:
        continue
    else:
        res.append(item[i])


# In[119]:


len(res)


# In[134]:


data.replace('null',100,inplace=True)


# In[148]:


data421=data[data['itemId']==421]


# In[152]:


data421.sort_values('recordTime')


# In[154]:


import pymysql
 
# 打开数据库连接
# db = pymysql.connect("58.16.78.136:30306","root",None,"predictvalue" )
d=pymysql.connect(db='aiops_monitor', user='root', passwd='1234', host='58.16.78.136', port=23306)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = d.cursor()
 
# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
da = cursor.fetchone()
 
print ("Database version : %s " % da)



# In[156]:


import fbprophet as fb

count=5401
for itemid in res[54:]:
    print('开始itemid为%d'% itemid)
    Fb=fb.Prophet()
    data1=data[data['itemId']==itemid].loc[:,['recordTime','value']]
    data1=data1.sort_values('recordTime')
    data1['recordTime']=pd.to_datetime(data1['recordTime'], unit='s')
    data1.columns=['ds','y']
    Fb.fit(data1)
    Pre=Fb.make_future_dataframe(freq='T',periods=100,include_history=False)
    forcasts=Fb.predict(Pre)
    forcast=forcasts.loc[:,['ds','trend','yhat_lower','yhat_upper']]
    date=list(forcast['ds'])
    trend=list(forcast['trend'])
    yhat_lower=list(forcast['yhat_lower'])
    yhat_upper=list(forcast['yhat_upper'])
    print(forcast)
    print('开始插入Itemid %d'%itemid)
    for i in range(len(date)):
        count+=1
        sql = "insert into predict(timestamp,id,value,l_value,h_value,item_id) values('%s','%d','%f','%f','%f','%d')" % (date[i],count,trend[i],yhat_lower[i],yhat_upper[i],itemid)
        try:
           # 执行SQL语句
           cursor.execute(sql)
           # 提交修改
           d.commit()
        except:
       # 发生错误时回滚
           d.rollback()

# 关闭数据库连接
# d.close()
# In[102]:


# import time
# import datetime
# def timestamp_2_time(timestamp):
#     temp = time.localtime(timestamp)
#     temp = time.strftime("%Y-%m-%d %H:%M:%S", temp)
#     time_data = pd.to_datetime(temp)
#     return time_data
# data['recordTime'] = data['recordTime'].apply(timestamp_2_time)
# temp_date= datetime.datetime(2019, 5, 21, 11, 0, 0)
# temp = data[data['recordTime'] >= temp_date]
# a = temp[temp['itemId'] == 258]
# print(a)
#
#
# # In[103]:
#
#
# left_date= datetime.datetime(2019, 5, 17, 0, 0, 0)
# right_date = left_date + datetime.timedelta(days=1)
# print(left_date, right_date)
# res_data = data[(data['recordTime'] <= right_date) & (data['recordTime'] >= left_date)]
# res_data


# In[ ]:




