def dfs(nums,index,target,res,path):
    if target<0: return
    if target==0 and len(path)==3:
        res.append(path)
        return
    
    for i in range(index,len(nums)):
        # 如果下一个数比当前所需要的targe大，就直接断掉
        if nums[i]>target: break
        # 如果有重复值就，去掉这个数
        if i>index and nums[i]==nums[i-1]:continue
        
        dfs(nums,i+1,target-nums[i],res,path+[nums[i]])
        

nums=[10,1,1,1,1,1,1,2,7,6,1,1,5]
nums.sort()
print(nums)
target=8
res=[]
dfs(nums,0,target,res,[])
print(res)