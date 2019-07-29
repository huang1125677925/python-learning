'''
https://my.oschina.net/yangyanxing/blog/296052

https://blog.csdn.net/houyanhua1/article/details/78236514

'''

from multiprocessing import Process, Queue,Pool,Manager
import os, time, random

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.' % value)
            time.sleep(random.random())
        else:
            break

def queue_process():
	# 父进程创建Queue，并传给各个子进程：
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	# 启动子进程pw，写入:
	pw.start()
	# 等待pw结束:
	pw.join()
	# 启动子进程pr，读取:
	pr.start()
	pr.join()
	# pr进程里是死循环，无法等待其结束，只能强行终止:
	print('所有数据都写入并且读完')

def queue_pool():
	manager = Manager()
	# 父进程创建Queue，并传给各个子进程：
	q = manager.Queue()
	p = Pool()
	pw = p.apply_async(write, args=(q,))
	time.sleep(0.5)
	pr = p.apply_async(read, args=(q,))
	p.close()
	p.join()


def array_process():
	manager = Manager()
	# 父进程创建Queue，并传给各个子进程：
	q = manager.Array()
	p = Pool()
	pw = p.apply_async(write, args=(q,))
	time.sleep(0.5)
	pr = p.apply_async(read, args=(q,))
	p.close()
	p.join()



if __name__=='__main__':
	queue_process()
	queue_pool()