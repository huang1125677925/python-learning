import pandas as pd
import matplotlib.pyplot as plt


count = 0

x=20
i=12
y=2

# raw_data = pd.read_csv(
#     '/Users/huangchuang/Documents/GitHub/linux_python/abnormal/train_test_data/kpi' + str(i) + '.csv')
#
# raw_data.drop(['Unnamed: 0', 'KPI ID'], axis=1, inplace=True)
#
# a = list(raw_data[raw_data['label'] == 1].index)

data = pd.read_csv('kpi' + str(i) + 'detect.csv')

print(data.info())

# detect_abnormal = raw_data.loc[list(data['index']), :]
#
# # ll = pd.value_counts(detect_abnormal['label'])
# print(raw_data.shape)
#
# print(data.shape)
#
# index=[]
# detect_index1=[]
# dd=list(data['index'])
# for i in range(1,len(dd)):
#
#     if dd[i]-1==dd[i-1]:
#         continue
#     else:
#         detect_index1.append(dd[i])
#
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
#
# print(len(index))
#
# print(len(detect_index1))


# for i in detect_index1:
#     plt.title('detect_abnormal {}'.format(i))
#     raw_data.loc[i-60:i+60,'value'].plot()
#     plt.scatter(i,raw_data.loc[i,'value'],color='r')
#     plt.show()
    
# for j in index:
#     plt.title('raw_abnormal {}'.format(j))
#     raw_data.loc[j - 60:j + 60, 'value'].plot()
#     plt.scatter(j, raw_data.loc[j, 'value'], color='r')
#     plt.show()
temp=[]
# for i in detect_index1:
#     for j in index:
#         if i>j-15 and i<j+15:
#             temp.append(i)
#             count=count+1
#             break
# plt.figure(figsize=(100,100),dpi=200)
# for x in index:
#     count = count + 1
#     plt.subplot(10,10,count)
#     raw_data.loc[x-30:x+30,'value'].plot()
#     if raw_data.loc[x,'label']==1:
#         plt.scatter(x,raw_data.loc[x,'value'],color='r')
#     else:
#         plt.scatter(x, raw_data.loc[x, 'value'], color='b')
#
#
#     print(count)
#
# plt.savefig('kpi'+str(1212)+'.png')




