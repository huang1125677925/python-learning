import platform
import sys
import os
import time
from multiprocessing import Pool, Lock, Value, Manager

count = [0]
lock = Lock()


def get_os():
    '''''
    get os 类型
    '''
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"


def ping_ip(ip_str, mylist):
    cmd = ["ping", ip_str]
    output = os.popen(" ".join(cmd))
    
    for line in output:
        if 'icmp_seq=0 ttl=' in line:
            # num.value =num.value +1
            mylist.append(ip_str)
            print(ip_str)
            return
        if 'timeout' in line:
            return
        # if str(line).upper().find("TTL") >= 0:
        #     flag = True
        #     bre


def find_ip(ip_prefix):
    '''''
    给出当前的127.0.0 ，然后扫描整个段所有地址
    ''''ping 192.168.2.30'
    p = Pool(processes=10)
    # num = Value("d", 1)
    for i in range(1, 256):
        ip = '%s.%s' % (ip_prefix, i)
        # threading.start_new_thread(ping_ip, (ip,))
        p.apply_async(ping_ip, (ip, mylist))
    
    p.close()
    p.join()


if __name__ == "__main__":
    start = time.time()
    mylist = Manager().list()
    print("start time %s" % time.time())
    # commandargs = sys.argv[1:]
    commandargs = '192.168.1.1'
    args = "".join(commandargs)
    
    ip_prefix = '.'.join(args.split('.')[:-1])
    find_ip(ip_prefix)
    print(len(mylist))
    print(mylist)
    print(time.time() - start)