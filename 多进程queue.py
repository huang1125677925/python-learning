# coding=utf-8
from multiprocessing import Queue, Process
from queue import Empty as QueueEmpty
import random


def getter(name, queue):
    print('Son process %s' % name)
    while True:
        try:
            value = queue.get(True, 10)
            # block为True,就是如果队列中无数据了。
            #   |—————— 若timeout默认是None，那么会一直等待下去。
            #   |—————— 若timeout设置了时间，那么会等待timeout秒后才会抛出Queue.Empty异常
            # block 为False，如果队列中无数据，就抛出Queue.Empty异常
            print("Process{0} getter put: {1}".format(name, value))
        except QueueEmpty:
            break


def putter(name, queue):
    print("Son process %s" % name)
    for i in range(0, 10):
        value = random.random()
        queue.put(value)
        # 放入数据 put(obj[, block[, timeout]])
        # 若block为True，如队列是满的：
        #  |—————— 若timeout是默认None，那么就会一直等下去
        #  |—————— 若timeout设置了等待时间，那么会等待timeout秒后，如果还是满的，那么就抛出Queue.Full.
        # 若block是False，如果队列满了，直接抛出Queue.Full
        print("Process--- {0}----- putter put: {1}".format(name, value))


if __name__ == '__main__':
    queue = Queue()
    getter_process = Process(target=getter, args=("Getter", queue))
    putter_process = Process(target=putter, args=("Putter", queue))
    putter_process1 = Process(target=putter, args=("Putter1", queue))

    putter_process.start()
    putter_process1.start()


    getter_process.start()

    putter_process.join()
    putter_process1.join()
    getter_process.join()