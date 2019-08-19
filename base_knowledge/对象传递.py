def f(x):
    x.append(4)
    print(id(x))
a=[1,2,3]
print(id(a))
f(a)