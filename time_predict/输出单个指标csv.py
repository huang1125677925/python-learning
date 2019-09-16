from time_predict import read_data1
import matplotlib.pyplot as  plt


data_read=read_data1.ReadData()

data=data_read.read_data(9932,'2019-07-25 12:00:00','2019-09-20 15:00:00')

# print(data.shape)
data.dropna(axis=1)
data['value']=list(map(float,data['value']))
data.to_csv('9932.csv')