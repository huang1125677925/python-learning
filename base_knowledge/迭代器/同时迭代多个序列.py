from itertools import zip_longest
x=list(range(10))
y=list(range(10,21))

for a,b in zip(x,y):
    print(a,b)


for i in zip_longest(x,y,fillvalue=0):
    print(i)
    
    

print(dict(zip(x,y)))
    
