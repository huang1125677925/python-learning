from sklearn.preprocessing import MinMaxScaler
    
data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
import numpy as np
d=np.array(data)

dd=np.array([0,99]).reshape(-1,1)


print(dd)
scaler = MinMaxScaler()
scaler.fit(dd)
dd=scaler.transform(dd)

print(scaler.data_max_)
print(scaler.data_min_)

dd=np.append(dd,[[1.2],[2.0]],axis=0)
print(dd)
d=scaler.inverse_transform(dd)
print(d)
print(dd.reshape(1,-1)[0])
