import pandas as pd
l=list(range(1,30))
for k in l:
    data = pd.read_csv(
        '/Users/huangchuang/Documents/GitHub/linux_python/abnormal/train_test_data/kpi' + str(k) + '.csv')
    
    data.drop(['Unnamed: 0', 'KPI ID'], axis=1, inplace=True)
    # print(data.head())
    print(k,data.loc[2,'timestamp']-data.loc[1,'timestamp'])