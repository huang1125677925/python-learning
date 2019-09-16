import pandas as pd
import matplotlib.pyplot as plt
from time_predict import read_data1
data_read=read_data1.ReadData()

data=data_read.read_data(57,'2019-07-25 12:00:00','2019-09-20 15:00:00')
print(data.shape)


timestamp1=list(map(str,pd.date_range(data['timestamp'].min(),data['timestamp'].max(),freq='T')))

data1=pd.DataFrame(data=timestamp1,columns=['timestamp'])

print(data1.shape)

data2=data1.merge(data,left_on='timestamp',right_on='timestamp',how='left')
print(data2[data2['value'].isna()])
print(data.tail(200))


# data2['value'].plot()
# plt.show()
# data['value'].plot()
# plt.show()






