if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pymongo
    import pandas as pd
    import statsmodels.api as sm
    
    ma = Statistic()
    
    myclient = pymongo.MongoClient('10.1.11.14:27017')
    mydb = myclient["aiops"]
    mycol = mydb["item"]
    
    itemid = []
    query_id = mycol.distinct('itemId')
    for item in query_id:
        print(item)
        itemid.append(int(item))
    
    i = 0
    plt.figure(figsize=(100, 100), dpi=200)
    temp = []
    for id in itemid:
        i = i + 1
        myquery = {"itemId": id, "recordTime": {'$gte': '2019-07-29 05:00:00', '$lt': '2019-07-29 10:00:00'}}
        query_data1 = mycol.find(myquery, {"value": 1})
        
        data = []
        for x in query_data1:
            data.append(float(x.get('value')))
        print('数据采集完成--{}'.format(id))
        
        if len(data) < 10:
            print('数据太少--{}'.format(id))
            print(data)
            continue
        # x_vals = list(range(len(data)))
        # x_vals1 = []
        # data1 = []
        # for i in range(100, len(data)):
        #     if ma.predict(data[:i]) == 0:
        #         x_vals1.append(i - 1)
        #         data1.append(data[i - 1])
        
        # plt.plot(x_vals, data, 'k', label='Softplus', linewidth=2)
        # plt.scatter(x_vals1, data1, c='r', linewidth=2)
        # plt.title('statistic algorithm')
        # plt.show()
        # d=pd.DataFrame(data=data, columns=['data'])
        # d['feature']=pd.cut(d['data'],bins=10)
        # bin_data_feature=d.groupby(by='feature')
        # feature_group=dict(list(bin_data_feature))
        # temp=set()
        
        # for item in feature_group.keys():
        #     temp.add(item.left)
        #     temp.add(item.right)
        #     print(feature_group[item].shape)
        
        plt.subplot(25, 25, i)
        plt.title("{}".format(id))
        plt.xticks([])
        plt.yticks([])
        plt.acorr(data, usevlines=True, normed=True, maxlags=10, lw=2)
        # plt.hist(data, bins=20)
        # plt.boxplot(data,sym='o')
        
        print('{}的图片画图完毕'.format(id))
    
    plt.savefig('自相关.png')