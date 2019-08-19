import pandas as pd
import matplotlib.pyplot as plt

l=list(range(2,6))+list(range(9,27))+list(range(28,30))
count=0

for i in l:

    raw_data = pd.read_csv('/Users/huangchuang/Documents/GitHub/linux_python/abnormal/train_test_data/kpi'+str(i)+'.csv')
    
    raw_data.drop(['Unnamed: 0', 'KPI ID'], axis=1, inplace=True)
    
    a = list(raw_data[raw_data['label'] == 1].index)
    
    
    data=pd.read_csv('kpi'+str(i)+'detect.csv')
    
    
    
    detect_abnormal=raw_data.loc[list(data['index']),:]
    
    
    ll=pd.value_counts(detect_abnormal['label'])
    
    
    
    if len(ll)>0:
        
        print('kpi{0} accurate rate is {1}'.format(i,ll[1]/sum(ll)))
    else:
        continue
    
    
    
