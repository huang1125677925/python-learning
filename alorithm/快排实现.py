'''
python代码比其他语言简直简洁太多了
--------------------------------
算法名：快排
---------------------------------
三元运算符的实现方式
x if x>y else y
'''

def quicksort(array):

	less=[];greater=[]

	if len(array)<=1:
		return array

	pivot=array.pop()

	for x in array:
		if x<=pivot:less.append(x)
		else: greater.append(x)

	return quicksort(less)+[pivot]+quicksort(greater)



print(quicksort([9,8,4,5,32,64,2]))
x=4;y=10


print(x if x>y else y)

# python中单双引号没有明显差异
print('nihao ,"nihao"')
print("nihao ,\"nihao\"")