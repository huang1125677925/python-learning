from sklearn.preprocessing import MinMaxScaler
    
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
import numpy as np
d=np.array(data)
print(d[:,0])

dd=np.array(range(100)).reshape(-1,1)


print(dd)
scaler = MinMaxScaler()
print(scaler.fit(dd))
MinMaxScaler(copy=True, feature_range=(0, 1))
print(scaler.data_max_)

print(scaler.transform(dd))
