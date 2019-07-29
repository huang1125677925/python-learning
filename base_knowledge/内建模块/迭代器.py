import itertools


a=[2,2,7,5,4,3,2,2,1]

b=sorted(a,reverse=True)

# print("通过下标逆序遍历1：")
# for i in a[::-1]:
#     print(i, end=" ")
# print("\n通过下标逆序遍历2：")
# for i in range(len(a)-1,-1,-1):
#     print(a[i], end=" ")
# print("\n通过reversed逆序遍历：")
# for i in reversed(a):
#     print(i, end=" ")

print(a)


l=len(a)
temp=0
for i in range(l-1,-1,-1):
	print(i)
	if a[i]>a[i-1]:
		temp=i-1

		break
for i in range(l-1,temp,-1):
	if a[i]>a[temp]:
		print(i)
		a[temp],a[i]=a[i],a[temp]
		break
print(a)

