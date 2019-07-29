#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def print_time(self,threadName, delay, counter):
        while counter:
            if exitFlag:
                (threading.Thread).exit()
            time.sleep(delay)
            print("%s: %d" % (threadName, counter))
            counter -= 1
    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print("Starting " + self.name)
        self.print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)


# 为什么会存在这种两个输出在同一行的情况，这有点不可解释，有两个线程

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1)

# 开启线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
# 
print("Exiting Main Thread")