n=9
d=[1 for _ in range(n)]
f=[]
for i in range(1,n):
    for j in range(i):
        if f[j]<=f[i] and d[i]<d[j]+1:
            d[i]=d[j]+1
        
return max(d)

# 都是同样的套路，后边的状态需要用到前面的状态