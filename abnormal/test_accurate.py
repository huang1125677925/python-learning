# import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import os
import pandas as pd
from multiprocessing import Pool


def data_prepare(start_index, end_index, data):
    data_mongo = []
    for i in range(1, 7):
        start_index = start_index - 1440
        end_index = end_index - 1440
        a=list(data.loc[start_index:end_index + 1, 'value'])
        data_mongo.append(a)
    
    return data_mongo


def seven_check_method(data,index):
    '''
    需要过去同期7个点
    :param l:
    :param value:
    :param threshold:
    :param count:
    :return:
    '''
    l=list(data.loc[index-8:index, 'value'])
    value=l[-1]
    num = 0
    mean = np.mean(l[:-1])
    for i in l:
        if abs(value - i) > mean:
            num += 1
    
    if num > 3:
        return True
    else:
        return False


def ewma_check_method(index,data):
    '''
    需要过去30分钟数据
    :param l:
    :return:
    '''
    l=read_pandas(index - 30, index, data)
    d = pd.Series(l)
    exp = d.ewm(span=5, adjust=True).mean()
    staDev = d.ewm(span=5, adjust=True).std()
    if abs(l[-1] - exp.values[-1]) > 3 * staDev.values[-1]:
        return True
    else:
        return False


def sameperiod_seven_point_check_method(data,index, value, max_threshlod=1.5, min_threshlod=0.5):
    '''
    需要过去七个点
    :param l:
    :param value:
    :param max_threshlod:
    :param min_threshlod:
    :return:
    '''
    data_mongo = data_prepare(index - 10, index, data)
    l=[item[-1] if item else np.mean(data_mongo) for item in data_mongo]
    if value > max(l) * max_threshlod or value < min(l) * min_threshlod:
        return True
    else:
        return False


def amplitude_check_method(data,index, value):
    '''
    需要过去七对同期
    :param l:
    :param value:
    :return:
    '''
    data_mongo = data_prepare(index - 10, index, data)
    l = [item[-2:] for item in data_mongo]
    
    def cal_apmlitude(value):
        
        return round(abs((value[1] - value[0] + 1)) / (value[0] + 1), 3)
    
    temp = []
    for item in l:
        temp.append(cal_apmlitude(item))
    now = cal_apmlitude(value)
    if now > max(temp):
        return True
    else:
        return False


def xigema_check(data,index1,index=4):
    '''
    可以把时间锁定在过去30分钟

    :param X:
    :param index:
    :return:
    '''
    X=read_pandas(index1 - 30, index1, data)
    if abs(X[-1] - np.mean(X[:-1])) > index * np.std(X[:-1]):
        return True
    return False


def threshold_value(X, index=3):
    min_value = np.mean(X) - index * np.std(X)
    max_value = np.mean(X) + index * np.std(X)
    
    return min_value, max_value

def dynamic_threshold(data,index, value):
    data_mongo = data_prepare(index - 10, index, data)
    l = [x for item in data_mongo for x in item]
    min_value, max_value = threshold_value(l)
    
    if value < min_value or value > max_value:
        return True
    else:
        return False


def read_pandas(start_index, end_index, data):
    return list(data.loc[start_index:end_index + 1, 'value'])


def check(k):
    '''
    把数据处理流程都写进各方法体中，
    然后搞个类来进行调用
    :return:
    '''
        
    data = pd.read_csv(
        '/root/train_test_data/kpi' + str(k) + '.csv')
    
    data.drop(['Unnamed: 0', 'KPI ID'], axis=1, inplace=True)
    
    temp = []
    
    if data.shape[0] < 9000:
        return 0
    
    for i in range(9000, data.shape[0]):
        
        if i % 10000 == 0:
            print('fie{0}-----{1}'.format(k, i))
             
        if sameperiod_seven_point_check_method(data,i,data.loc[i,'value']):
            temp.append(i)
            
    abnoraml=data.loc[temp, 'label']
    res=pd.value_counts(abnoraml)
    find_abnormal=abnoraml.shape[0]
    raw_abnormal=data[data['label']==1]
    find_abnormal_set=set(temp)
    raw_abnormal_set=raw_abnormal.index
    
    
    res_set=raw_abnormal_set.intersection(find_abnormal_set)
    return [k,len(res_set)/len(raw_abnormal_set),find_abnormal,raw_abnormal.shape[0],res]
    

if __name__ == '__main__':
    start=time.time()
    p = Pool(29)  # 进程池中从无到有创建三个进程,以后一直是这三个进程在执行任务
    res_l = []
    for i in range(1, 30):
        res = p.apply_async(check, args=(i,))
        res_l.append(res)
    
    p.close()
    p.join()
    for res in res_l:
        print(res.get())  # 使用get来获取apply_aync的结果,如果是apply,则没有get方法,因为apply是同步执行,立刻获取结果,也根本无需get
    print(time.time()-start)
