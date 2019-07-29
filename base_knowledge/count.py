from collections import Counter


class Solution:
	def removeDuplicateLetters(self, s: str) -> str:
		a = dict(Counter(s))
		temp = []
		s = list(s)
		for i in s:
			if temp == []:
				temp.append(i)
			elif i in temp:
				a[i]-=1
				continue
			elif temp[-1]>i and a[temp[-1]]==1 and i not in temp:
				temp.append(i)
			elif temp[-1] > i :
				while temp and a[temp[-1]]>1 and temp[-1] > i:
					temp.pop()
				temp.append(i)
			elif temp[-1] < i and i not in temp:
				temp.append(i)

		return ''.join(temp)




if __name__ == '__main__':
	print(Solution().removeDuplicateLetters("cbacdcbc"))
