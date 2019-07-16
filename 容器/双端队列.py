from collections import deque


data = deque([10], maxlen=4)

print(data)

data.insert(2, 9)

print(data)

data.append(11)

print(data)
