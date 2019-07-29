'''
[莫凡讲多进程]https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/5-pool/
close 说是不会有新的进程加入到进程池的意思就是，每当正在运行的进程结束，就不再返回进程池，这样启动起来的子进程全部结束，就是用join
https://www.cnblogs.com/kaituorensheng/p/4465768.html

https://blog.csdn.net/jinping_shi/article/details/52433867

'''

from multiprocessing import Pool
import os, time


def job(x):
    return x*x


def muticore():
    pool=Pool(processes=3)
    res=pool.map(job,range(10))

    print(res)

    res=pool.apply_async(job,(2,))

    print(res.get())

    muti_res=[pool.apply_async(job,(i,)) for i in range(9)]

    print([res.get() for res in muti_res])

    pool.close()
    pool.join()


def func(msg,i):
    print("start----{0}---{1}--{2}".format(time.time(), msg,i))
    print("msg:", msg)
    time.sleep(1)


def apply_async():
    pool = Pool(processes = 3)
    while 1:
        for i in range(4):
            msg = "hello %d" %(i)
            pool.apply_async(func, (msg, 1,))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("Sub-process(es) done.")

def apply():
    pool = Pool(processes = 3)
    for i in range(4):
        msg = "hello %d" %(i)
        pool.apply(func, (msg, 1,))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print("Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~")
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print("Sub-process(es) done.")



# p.apply_async(pro_do, (i,))
if __name__ == "__main__":
    apply_async()