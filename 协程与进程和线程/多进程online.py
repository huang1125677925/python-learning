#!/usr/tools/env python
# -*- coding: UTF-8 -*-

from multiprocessing import Pipe, Process, cpu_count


PROCESS_NUM = cpu_count()

def pre():
    print("-------pre------")

def pro():
    print("---------pro-----------")
def main():
    """
    模型更新进程
    """
    son_p_data_model = Process(target=pre)
    son_p_data_model.start()
    son_p_data_model.join()

    # 初始化管道
    out_pipe = [None] * PROCESS_NUM
    in_pipe = [None] * PROCESS_NUM
    son_p_data = [None] * PROCESS_NUM

    # 数据处理进程
    for i in range(PROCESS_NUM):
        out_pipe[i], in_pipe[i] = Pipe(True)
        son_p_data[i] = Process(target=pro)

    for i in range(PROCESS_NUM):
        son_p_data[i].start()
        # 等pipe被fork 后，关闭主进程的输出端
        # 这样，创建的Pipe一端连接着主进程的输入，一端连接着子进程的输出口
        out_pipe[i].close()

    # distribute_pipe(in_pipe)

    for i in range(PROCESS_NUM):
        son_p_data[i].join()



"""
在线异常检测主程序入口
"""
if __name__ == "__main__":
    main()