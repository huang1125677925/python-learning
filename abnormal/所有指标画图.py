import pandas as pd
import matplotlib.pyplot as plt

temp=[]

for i in range(1,30):
    raw_data = pd.read_csv(
        '/Users/huangchuang/Documents/GitHub/linux_python/abnormal/train_test_data/kpi' + str(i) + '.csv')
    
    # plt.title('{} itemid'.format(2))
    # raw_data.drop(['timestamp','Unnamed: 0'],axis=1,inplace=True)
    # raw_data.boxplot()
    # raw_data['value'].plot()
    # abnoraml=list(raw_data[raw_data['label']==1].index)
    # abnormal_data=raw_data.loc[abnoraml,'value']
    # plt.scatter(abnoraml,list(raw_data[raw_data['label']==1]['value']),color='r')
    
    # plt.xticks(list(range(1,30)), xlabel, rotation='vertical')
    
    # plt.show()
    
    print('---------------',i)
    describe=raw_data.loc[:7000,:].describe()['value']
    print(describe)
    # if describe['max']>25*describe['std']:
    #     print(i)