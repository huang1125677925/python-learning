from itertools import chain
import abnormal.read_data

a=[1,2,3,4,5]
b=('a','b','c')
c={'a':1,'d':10}
d=[(1,2)]

for i in chain(a,b,c.items(),d):
    print(i)