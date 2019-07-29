from collections import deque
class LRUCache:

	def __init__(self, capacity: int):
		self.data=deque(maxlen=capacity)
		self.d_data={}

	def get(self, key: int) -> int:
		if key in self.d_data.keys():
			self.data.remove(key)
			self.data.append(key)
			return self.d_data[key]
		else:
			return -1
	def put(self, key: int, value: int) -> None:
		if len(self.data)==self.data.maxlen:
			if key not in self.d_data.keys():
				temp=self.data.popleft()
				self.d_data.pop(temp)
				self.data.append(key)
				self.d_data[key]=value
			else:
				self.data.remove(key)
				self.data.append(key)
				self.d_data[key]=value

		else:
			if key not in self.d_data.keys():
				self.data.append(key)
				self.d_data[key] = value
			else:
				self.data.remove(key)
				self.data.append(key)
				self.d_data[key] = value


from collections import OrderedDict

class LRUCache(OrderedDict):

	def __init__(self, capacity):
		self.capacity = capacity

	def get(self, key):
		if key not in self:
			return - 1

		self.move_to_end(key)
		return self[key]

	def put(self, key, value):
		if key in self:
			self.move_to_end(key)
		self[key] = value
		if len(self) > self.capacity:
			self.popitem(last=False)


if __name__ == '__main__':


	cache = LRUCache( 2 )

	cache.put(1, 1)
	cache.put(2, 2)
	cache.put(2,1)
	cache.get(1);
	cache.put(3, 3);
	cache.get(2)
	cache.put(4, 4)
	cache.get(1)
	cache.get(3)
	cache.get(4)

