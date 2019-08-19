# -*- coding:utf-8 -*-

import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


import matplotlib.pyplot as plt

from matplotlib.font_manager import *
myfont = FontProperties(fname='/usr/local/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf/simhei.ttf')
matplotlib.rcParams['axes.unicode_minus']=False




# files=os.listdir('/Users/huangchuang/Documents/GitHub/linux_python/abnormal/train_test_data')
files=os.listdir('train_test_data')
sourece='train_test_data'
destination='kpi'
count=1
# for file in files:
#     os.rename(sourece+'/'+file,sourece+'/'+destination+str(count)+'.csv')
#     count+=1
temp=[]
noraml_data=[]
col=[]
l=len(files)
for file in files:
    data=pd.read_csv(sourece+'/'+file)
    d=pd.value_counts(data['label'])
    
    temp.append(d[1])
    noraml_data.append(d[0])
    col.append(os.path.splitext(file)[0])
    


    

# plt.title('清华比赛数据29个指标(异常数目/整体数目)视图————可作为参考',fontproperties=myfont)
#
# plt.plot(list(range(1,l+1)),temp)
# plt.show()