def fun_var_kwargs(farg,**kwargs):
    print("arg:",farg)
    for key in kwargs:
        print("another keyword arg:(%s,%s)"%(key,kwargs[key]))



fun_var_kwargs(farg=9,huang=4,chuang=10)