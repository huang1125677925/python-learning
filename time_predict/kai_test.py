import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

with open('request-number-data1.txt','r') as f:
    a=f.readlines()[0]
    d=eval(a)

print(list(d))
data=pd.DataFrame(list(d),columns=['timestamp','value'])
print(data)
def f(x):
    return float(x)
data['value']=data['value'].apply(f)
print(type(data['timestamp'][0]))

print(data['timestamp'].max()-data['timestamp'].min())
# plt.plot(list(range(data.shape[0])),list(data['value']))
# plt.boxplot(coloumns=['value'])
# plt.show()
plt.figure(figsize=(15,6))
plt.hist(data['value'],bins=10)
plt.show()

def data_prepare(data):
    check_data = []

    start_date = 1565599020
    end_date = 1565599320

    data1 = data[(data['timestamp'] > start_date) & (data['timestamp'] <= end_date)]['value']
    print(data1)

    check_data.extend(list(data1))

    print('----------------')

    data_mongo = []
    for i in range(1, 18):
        start_date = start_date - 1200
        end_date = end_date - 1200

        data1 = data[(data['timestamp'] > start_date) & (data['timestamp'] <= end_date)]['value']
        print(i,data1)

        data_mongo.extend(list(data1))

        print('----------------')
    print(len(data_mongo))
    return data_mongo, check_data


def threshold_value(X, index=3):
    
    min_value = np.mean(X) - index * np.std(X)
    max_value = np.mean(X) + index * np.std(X)

    return min_value, max_value


def main():
    data_history, data_check = data_prepare(data)
    l=list(range(1,6))
    indexl=l*17
    print(indexl)
    print(len(data_history))
    plt.scatter(indexl,data_history)
    plt.scatter(l,data_check,color='r')
    plt.show()
    min_v, max_v = predict(data_history)
    print(min_v,max_v)
    print(data_check)

    import seaborn as sns
    sns.set_palette("hls")  # 设置所有图的颜色，使用hls色彩空间
    sns.distplot(data_history, color="r", bins=30, kde=True)
    plt.show()
    for i in data_check:
        if i < min_v or i > max_v:
            print(i)
        else:
            print('not abnormal')


    iso=IForest()
    print(iso.predict(data_history+data_check,indexl+l))


if __name__ == '__main__':
    main()

