import pandas as pd
from time_predict import read_data1
data=pd.read_table('not_enough_data_id.txt',names=['id'])
a=read_data1.ReadData()
res=[]
for i in list(data['id']):
    print(i)
    d=a.read_data(int(i.split()[0]),'15 00:00:00','26 00:00:00')
    res.append([int(i.split()[0]),d['timestamp'].max(),d['timestamp'].min(),d.shape[0]])
    

print('开始导出文件')
pd.DataFrame(res,columns=['id','max_time','min_time','11_days_length']).to_csv('itmid.csv')
