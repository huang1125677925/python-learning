class Solution:
    def findUnsortedSubarray(self, nums) -> int:
        i, j = 0, len(nums) - 1
        if len(nums) <= 1:
            return 0
        while i < len(nums) - 1:
            if nums[i + 1] >= nums[i]:
                i += 1
            else:
                while i > 0:
                    if nums[i] == nums[i - 1]:
                        j -= 1
                    else:
                        break
                break
        while j > 0:
            if nums[j] >= nums[j - 1]:
                j -= 1
            else:
                while j < len(nums) - 1:
                    if nums[j] == nums[j + 1]:
                        j += 1
                    else:
                        break
                break
    
        if i < j:
            return j - i + 1
        else:
            return 0
        
print(Solution().findUnsortedSubarray([1,3,2,2,2]))