'''
所谓类变量与实例变量，其实在于初始化的时候，如何调用的
1、self.num_of_instance += 1
0
0
jack 1
lucy 1
-----------------------
2、Test.num_of_instance += 1
0
1
jack 2
lucy 2
-----------------------
这就变成了类变量，self和
'''

class Test(object):
	num_of_instance = 0

	def __init__(self, name):
		self.name = name
		Test.num_of_instance += 1


if __name__ == '__main__':
	print(Test.num_of_instance)  # 0
	t1 = Test('jack')
	print(Test.num_of_instance)  # 1
	t2 = Test('lucy')
	print(t1.name, t1.num_of_instance)  # jack 2
	print(t2.name, t2.num_of_instance)  # lucy 2