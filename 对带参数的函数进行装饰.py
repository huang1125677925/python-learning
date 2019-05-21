def deco(func):
    def __deco(a,b):
        print("befor called")
        ret=func(a,b)
        print("after called")
        return ret
    return __deco

@deco
def myfunc(a,b):
    print("myfunc(%s,%s) called"%(a,b))
    # return a+b

myfunc(1,2)
myfunc(9,8)