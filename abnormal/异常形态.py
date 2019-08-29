import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('/Users/huangchuang/Documents/GitHub/linux_python/abnormal/train_test_data/kpi3.csv')

print(data.columns)
print(data.shape)
data.drop(['Unnamed: 0',  'KPI ID'],axis=1,inplace=True)
print(data.head())

a=set(data[data['label']==1].index)
a.

print(data.index)


# a=list(data[data['label']==1].index)
#
# index=[]
#
#
# for i in range(1,len(a)):
#     if a[i]-1==a[i-1]:
#         continue
#     else:
#         index.append(a[i])
#
#
#
# print(index)




