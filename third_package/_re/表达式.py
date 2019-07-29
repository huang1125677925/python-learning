# https://blog.csdn.net/weixin_40907382/article/details/79654372

import re

a='shopeemobile.com'
for item in a:
	print(re.findall(r'*.com',a))

a={}

a['.']=True

print(a['.'])


print(type(5/3))
print(type(6/3))

# print(a[3:].index(1))
# print(list(map(lambda x,y:y-x,a[:-1],a[1:])))
#
#
# class Solution:
# 	def containsNearbyDuplicate(self, nums, k) -> bool:
# 		if k == 0:
# 			return False
# 		if len(nums) == 1:
# 			return False
# 		num = list(set(nums))
# 		if len(nums) == len(num):
# 			return False
# 		for item in num:
# 			if nums.count(item) == 1:
# 				continue
# 			temp = set()
# 			for i in range(len(nums)):
# 				temp.add(nums[i:].index(item) + i)
# 			temp = list(sorted(temp))
# 			r = min(list(map(lambda x, y: y - x, temp[:-1], temp[1:])))
# 			if r <= k:
# 				return True
#
# 		return False
#
# print(Solution().containsNearbyDuplicate([1,2,3,1,2,3],2))

