from multiprocessing import Pool
import os, time
start = time.time()

def pro_do(process_num):
    print("child process id is %d" %(os.getpid()))
    time.sleep(1)
    print("this is process %d" %(process_num))
# p.apply_async(pro_do, (i,))
if __name__ == "__main__":
    print("Current process is %d" %(os.getpid()))
    p = Pool()
    for i in range(5):
        p.apply_async(pro_do,(i,))
    p.close()
    # 禁止在增加新的进程
    p.join()
    print(time.time()-start)