class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        for i in range(1,len(nums)+1):
            for j in range(len(nums)-i+1):
                print(nums[j:j+i])
                if sum(nums[j:j+i])>=s:
                    return i
        return s
    
print(Solution().minSubArrayLen(15,[1,2,3,4,5]))