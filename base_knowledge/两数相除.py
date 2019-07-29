class Solution:
	def divide(self, dividend: int, divisor: int) -> int:
		if dividend==0:
			return 0
		temp=dividend//divisor
		print(temp)
		if abs(temp*divisor)<=abs(dividend):
			print(temp)
			a=-(2**31)
			b=(2**31-1)
			if a<= temp and temp<=b:
				return temp
			else:
				return 2**31-1

		else:
			return temp+1 if -2**31<=temp+1<=(2*31-1) else 2**31-1



a = 1
b = 2

h = a-b if a>b else a+b

print(h)

print(Solution().divide(2147483647,2))
print(2147483647//2)