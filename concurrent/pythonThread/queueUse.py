# 先进先出队列
import queue

# 最多接收10个数据
q = queue.Queue(2)

# put 向队列中添加数据
q.put(15)
q.put(59)

# 获取当前队列长度
print(q.qsize())
# q.put(3,timeout=2)
# 取出最前面的一个数据
print(q.get())


# 设置队列不阻塞(当队列满的时候再插入数据,直接报错)
q.put('PolarSnow', block=False)

print(q.get())
print(q.get())