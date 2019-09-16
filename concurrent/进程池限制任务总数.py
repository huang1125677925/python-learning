from multiprocessing import cpu_count, Pool

p = Pool(processes=cpu_count() , maxtasksperchild=2)

def f(x):
    print(x,x*x)
    return x*x

a=list(range(100))
p.map_async(f, a)





# print(b)

# from multiprocessing import Pool
#
# def f(x):
#     return x*x
#
# if __name__ == '__main__':
#     with Pool(5) as p:
#         print(p.map_async(f, [1, 2, 3]).get())
