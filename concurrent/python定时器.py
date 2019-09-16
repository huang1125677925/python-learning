import threading

def func1():
  print('Do something.')
  timer = threading.Timer(2, func1)
  timer.start()

def func2(a):
    #Do something
    print('Do something')
    a+=1
    print(a)
    print('当前线程数为{}'.format(threading.activeCount()))
    if a>5:
        return
    t=threading.Timer(5,func2,(a,))
    t.start()


if __name__ == '__main__':
    timer = threading.Timer(3600, func1)
    timer.start()