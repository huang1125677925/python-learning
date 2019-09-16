class Solution:
    def findMaxLength(self, nums) -> int:
        count,maxl=0,0
        d={}
        d[0]=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                if count not in d:
                    d[count]=i
                else:
                    maxl=max(maxl,i-d[count])
            else:
                count-=1
                if count not in d:
                    d[count]=i
                else:
                    maxl=max(maxl,i-d[count])
        return maxl
    
print(Solution().findMaxLength([0,1]))
