from time_predict import read_data1

a=read_data1.ReadData()

itemid=a.read_itemid()

for id in itemid:
    d=a.read_data(id,'15 00:00:00','26 00:00:00')
    if d.shape[0]>2000:
        d.to_csv('/Users/huangchuang/Desktop/itemid/'+str(id)+'.csv')
    else:
        print('{} not have the enough data'.format(id))
    

