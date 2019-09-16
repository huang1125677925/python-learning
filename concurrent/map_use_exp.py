import multiprocessing
import time
def job(x ,y):
    print(x*y)
    
    return x * y


def job1(z):
    print(z)
    return job(z[0], z[1])


if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=3)
    res = pool.map(job1, [(2, 3), (3, 4)])
    # time.sleep(1)
    
    print(res)

