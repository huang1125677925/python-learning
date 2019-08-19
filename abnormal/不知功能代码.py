from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
import pandas as pd

# df = pd.read_csv('../test1.csv', skipfooter=0)
# df.columns = ['time', 'data']
# df.dropna(inplace=True)
# df.index = pd.date_range(start='1949-01-31', end='1960-12-31', freq='M', )
# y = df.data
# model = SARIMAX(y[:120], order=(2, 2, 1), seasonal_order=(2, 1, 1, 12), freq='M').fit()
# # print(model.summary())
# y_pred = model.predict(start='1949-03-31', end='1960-12-31')
# plt.plot(y)
# plt.plot(y_pred)
# plt.legend(['y_true', 'y_pred'])
# plt.show()

if __name__ == "__main__":
    from aiops_detection_online.unsupervise import statistic, fourpecent
    import matplotlib.pyplot as plt
    import pymongo
    
    ma = statistic.Statistic()
    mb = fourpecent.FourPercent()
    
    myclient = pymongo.MongoClient('10.1.11.14:27017')
    mydb = myclient["aiops"]
    mycol = mydb["item"]
    
    j = 0
    itemid = []
    query_id = mycol.distinct('itemId')
    for item in query_id:
        itemid.append(int(item))
    
    print(len(itemid))
    plt.figure(figsize=(100, 100), dpi=200)
    
    for id in itemid:
        j = j + 1
        myquery = {"itemId": int(id), "recordTime": {'$gte': '2019-08-05 05:00:00', '$lt': '2019-08-05 18:00:00'}}
        query_data1 = mycol.find(myquery).sort('recordTime')
        
        data = []
        for x in query_data1:
            d = float(x['value'])
            data.append(d)
        print('数据采集完成--{}'.format(id))
        if len(data) < 10:
            print('数据太少--{}'.format(id))
            print(data)
            continue
        else:
            print('---------------------------------{}'.format(id))
        
        x_vals = list(range(len(data)))
        x_vals1 = []
        data1 = []
        for i in range(180, len(data)):
            if mb.predict(data[i - 180:i]) == 0:
                x_vals1.append(i - 1)
                data1.append(data[i - 1])
        
        plt.subplot(30, 30, j)
        plt.title("{}".format(id))
        plt.xticks([])
        plt.yticks([])
        plt.plot(x_vals, data, 'k', label='Softplus', linewidth=2)
        plt.scatter(x_vals1, data1, c='r', linewidth=2)
        
        print('{}--指标画图完成'.format(id))
    
    plt.savefig('指标图像.png')