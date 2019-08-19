from sklearn.datasets import  load_breast_cancer
cancer=load_breast_cancer()
from sklearn.preprocessing import StandardScaler
print(cancer)
scaler=StandardScaler()
scaler.fit(cancer.data)
x_scaled=scaler.transform(cancer.data)

print(x_scaled)