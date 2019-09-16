s=''
l=len(s)
d=[[0 for _ in range(l)] for _ in range(l)]
ans=0
def find_largest_sequence():
    for i in range(l):
        d[i][i]=1
        if i<l-1 and s[i]==s[i+1]:
            d[i][i+1]=1
            ans=2
    
    # 状态转移方程
    for i in range(3,l+1):
        for j in range(l-i+1):
            k=j+i-1
            if s[j]==s[k] and d[i+1][k-1]==1:
                ans=i
    
    return  ans
