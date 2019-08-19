import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import os




def data_prepare( start_index, end_index, data):
    data_mongo = []
    for i in range(1, 7):
        start_index = start_index- 1440
        end_index = end_index - 1440
        
        data_mongo.append(list(data.loc[start_index:end_index+1,'value']))
    
    return data_mongo


def seven_check_method( l, value):
    '''
    需要过去同期7个点
    :param l:
    :param value:
    :param threshold:
    :param count:
    :return:
    '''
    num = 0
    mean = np.mean(l)
    for i in l:
        if abs(value - i) > mean:
            num += 1
    
    if num > 3:
        return True
    else:
        return False


def ewma_check_method( l):
    '''
    需要过去30分钟数据
    :param l:
    :return:
    '''
    d = pd.Series(l)
    exp = d.ewm(span=5, adjust=True).mean()
    staDev = d.ewm(span=5, adjust=True).std()
    if abs(l[-1] - exp.values[-1]) > 3 * staDev.values[-1]:
        return True
    else:
        return False


def sameperiod_seven_point_check_method( l, value, max_threshlod=1.5, min_threshlod=0.5):
    '''
    需要过去七个点
    :param l:
    :param value:
    :param max_threshlod:
    :param min_threshlod:
    :return:
    '''
    if value > max(l) * max_threshlod or value < min(l) * min_threshlod:
        return True
    else:
        return False


def amplitude_check_method( l, value):
    '''
    需要过去七对同期
    :param l:
    :param value:
    :return:
    '''
    
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


def xigema_check( X, index=4):
    '''
    可以把时间锁定在过去30分钟

    :param X:
    :param index:
    :return:
    '''
    
    if abs(X[-1] - np.mean(X[:-1])) > index * np.std(X[:-1]):
        return True
    return False


def threshold_value(X, index=3):
    min_value = np.mean(X) - index * np.std(X)
    max_value = np.mean(X) + index * np.std(X)
    
    return min_value, max_value

def dynamic_threshold( l, value):
    min_value, max_value = threshold_value(l)
    if value < min_value or value > max_value:
        return True
    else:
        return False

def read_pandas(start_index,end_index,data):
    return list(data.loc[start_index:end_index+1,'value'])

def main():
    files = os.listdir('train_test_data')
    l=list(range(1,9))+list(range(14,30))
    for k in l:
    
        data = pd.read_csv('/Users/huangchuang/Documents/GitHub/linux_python/abnormal/train_test_data/kpi'+str(k)+'.csv')
        
        data.drop(['Unnamed: 0', 'KPI ID'], axis=1, inplace=True)
        
        a = list(data[data['label'] == 1].index)
        
        temp=[]
        
        if data.shape[0]<9000:
            continue
        
        for i in range(9000,data.shape[0]):
            
            if i%1000==0:
                print('fie{0}-----{1}'.format(k,i))
        
            index = i
            
        
            # 准备数据
            # 过去七天同期十分钟----包括与当前点相同的
            # 可用于振幅检测，同期动态阈值检测，同期七点检测
            data_mongo = data_prepare(index- 10, index, data)
        
            # 过去半个小时的数据------包括当前点
            # 可用于ewa检测，过去七点检测，3西格玛检测
            thirty_minutes_data = read_pandas(index - 30, index, data)
            
            # 细分为各算法所需数据
            # 包括当前点
            xigema_check_data = thirty_minutes_data
            ewma_data = thirty_minutes_data
            
            dynamic_threshold_data = [x for item in data_mongo for x in item]
            seven_point_data = thirty_minutes_data[-8:-1]
            sameperiod_seven_check_data = [item[-1] if item else np.mean(data_mongo) for item in data_mongo]
            amplitude_check_data = [item[-2:] for item in data_mongo]
            if data_mongo == []:
                continue
            
            if len(thirty_minutes_data) < 10:
                continue
                
            value=data.loc[index,'value']
            
            # 计算数据+融合
            methods = []
            count = 0
            if xigema_check_data and xigema_check(xigema_check_data):
                count = count + 1
                methods.append('xigema_check')
            if ewma_data and ewma_check_method(ewma_data):
                methods.append('ewma_check_method')
                count = count + 1
            if seven_point_data and seven_check_method(seven_point_data, value):
                methods.append('seven_check_method')
                count = count + 1
            if sameperiod_seven_check_data and sameperiod_seven_point_check_method(sameperiod_seven_check_data, value):
                count = count + 1
                methods.append('sameperiod_seven_point_check_method')
            if amplitude_check_data and amplitude_check_method(amplitude_check_data, thirty_minutes_data[-2:]):
                count = count + 1
                methods.append('amplitude_check_method')
            if dynamic_threshold_data and dynamic_threshold(dynamic_threshold_data, value):
                count = count + 1
                methods.append('dynamic_threshold')
            
            if count >=3:
                temp.append([index,methods,len(methods)])
                print(index,methods)
                
        
        find_abnormal=pd.DataFrame(data=temp,columns=['index','methods','Length'])
    
    
    
        a = list(data[data['label'] == 1].index)
    
        flag = []
    
        for i in range(1, len(a)):
            if a[i] - 1 == a[i - 1]:
                continue
            else:
                flag.append(a[i])
    
        max_min_abnoraml = []
    
        for item in flag:
            max_min_abnoraml.append([item - 20, item + 20])
    
        count = 0
    
        for i in list(find_abnormal['index']):
            for j in max_min_abnoraml:
                if i >= j[0] and i <= j[1]:
                    count = count + 1
                    continue
                    
        find_abnormal.to_csv('kpi'+str(k)+'detect.csv')
        
        
    
        print('{0}正确率：----------{1}'.format(k,count / find_abnormal.shape[0]))
    
        print('{0}召回率------------{1}'.format(k,count / len(flag)))
            
            
if __name__ == '__main__':
    main()