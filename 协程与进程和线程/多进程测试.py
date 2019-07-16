import requests
import time
import multiprocessing

start=time.time()

def request(_):
    url='http://127.0.0.1:5000'
    print('Waiting for',url)
    result=requests.get(url).text
    print('Get response from',url,'Result:',result)

cpu_count=multiprocessing.cpu_count()
print('Cpu count:',cpu_count)
pool=multiprocessing.Pool(cpu_count)
pool.map(request,range(100))

end=time.time()
print('Cost time:',end-start)