import pandas as pd

data=pd.read_csv('event_num_count.csv')

print(data[data['event_num']>30])