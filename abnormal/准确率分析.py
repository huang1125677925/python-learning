import pandas as pd
import matplotlib.pyplot as plt
temp=[]
with open('accurate.txt') as f:
    for item in f.readlines():
        t=item.split()
        temp.append([t[0],float(t[-1])])
        
print(temp)

data=pd.DataFrame(data=temp,columns=['itemid','value'])
# data['value'].plot()
# plt.xticks(list(range(data.shape[0])),list(data['itemid']),  rotation='vertical')
# plt.show()


print(list(data['itemid']))