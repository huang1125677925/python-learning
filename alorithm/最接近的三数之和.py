class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        res=1000000000000
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:continue
            j,k=i+1,len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if abs(s-target)<abs(res-target):
                    res=s
                if s>target:
                    k-=1
                    while j<k and nums[k]==nums[k+1]:k-=1
                elif s<target:
                    j+=1
                    while j<k and nums[j]==nums[j-1]:j+=1
                else:
                    k-=1
                    j+=1
        return res
    

print(Solution().threeSumClosest([-1,0,1,1,55],3))