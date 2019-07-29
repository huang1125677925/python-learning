from collections import deque


a=deque(range(100))

print(a)
for i in range(100):

    print(a.popleft())

print(len(a))
