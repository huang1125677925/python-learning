a=[6,0,8,2,1,5]

print(sorted(range(6),key=a.__getitem__))

print(a.__getitem__(2))
