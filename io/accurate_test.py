import pymongo
from sklearn.metrics import mean_squared_error
import time
import configparser
import numpy as np



def normalize_time_series_by_max_min(data):

    max_value = np.max(data)
    min_value = np.min(data)
    normalized_time_series = [0.0]*len(data)
    if max_value - min_value > 0:
        normalized_time_series = list((np.array(data) - min_value) / float(max_value - min_value))

    return normalized_time_series



def timeconvert(dt):


    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")

    timestamp = int(time.mktime(timeArray))

    return timestamp

def read_mongodb(itemid,timeup,timedown):
    '''

    :param itemid: 查询指标id
    :param timeup: 查询指标上限时间
    :param timedown: 查询指标下限时间
    :return: 查询数据列表，查询结果长度
    '''

    itemid = int(itemid)
    timeup1 = timeconvert(timeup)
    timedown1 =timeconvert(timedown)
    realdata = []
    predictdata=[]
    myquery = {"itemId":itemid,"recordTime": {'$gte': timeup1, '$lt': timedown1}}
    myquery1 = {"itemId": itemid, "predictTime": {'$gte': timeup, '$lt': timedown}}
    query_data=mycol.find(myquery, {"recordTime":1,"value": 1,'step':1})
    query_data1=mycol1.find(myquery1, {"predictTime":1,"value": 1})

    interval=0
    for x in query_data:
        temp=x.get('value')
        if temp=='null':
            print('真实数据中存在空值，请通知数据采集人员处理')
            return
        realdata.append(float(temp))
        interval=x.get('step')

    for x in query_data1:
        temp=x.get('value')
        if temp=='null':
            print('预测数据中存在空值，请通知数据采集人员处理')
            return
        predictdata.append(float(temp))
    predictdata_length =len(predictdata)
    realdata_length=len(realdata)
    if predictdata_length==0 and realdata_length==0:
        print("没有这个指标")
        return

    num=(timedown1-timeup1)//interval

    if predictdata_length!=realdata_length:
        print('此指标间隔是{0},取值个数应该为{1} 真实值个数是{2},预测值个数是{3}'.format(interval,num,realdata_length,predictdata_length))
        if predictdata_length<num:
            print("预测数据不够，请通知预测人员处理----{0}".format(predictdata_length))
        elif predictdata_length>num:
            print("预测数据超出，请通知预测人员处理----{0}".format(predictdata_length))
        if len(realdata)<num:
            print('真实数据不够，请通知数据采集人员处理----{0}'.format(realdata_length))
        elif len(realdata)>num:
            print("真实数据超出，请通知数据采集人员处理----{0}".format(realdata_length))

        return

    realdata=normalize_time_series_by_max_min(realdata)
    predictdata=normalize_time_series_by_max_min(predictdata)

    mse = mean_squared_error(predictdata, realdata)
    if mse>0.5:
        print("预测存在极大偏差，需要通知预测人员检查")
    elif mse<0.5 and mse>0.1:
        print("预测效果一般，也需要调整")
    else:
        print("预测效果非常好")

# 读取配置参数文件，参数与代码分离
cf=configparser.ConfigParser()
cf.read('test.ini')

# 连接数据库
myclient = pymongo.MongoClient(cf.get('real_mongodb','ip'))
mydb = myclient["test"]
mycol = mydb["item"]
mycol1=mydb["predict"]
while True:
    # 读取输入并读取原始数据和预测数据，处理
    rawinput=input("请输入id,想要查询的时间段,日期格式为%Y-%m-%d %H:%M:%S:")
    temp=rawinput.split(',')
    if len(temp)!=3:
        print("---------输入格式有误-----------")
        print("---------输入格式有误-----------")
        continue
    itemid,timeup,timedown=temp

    read_mongodb(itemid,timeup,timedown)

