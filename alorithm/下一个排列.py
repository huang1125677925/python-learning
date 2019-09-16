class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums[::-1]==sorted(nums):
            nums.sort()
            return
        index=0
        for i in range(len(nums)-1,0,-1):
            if nums[i]<=nums[i-1]:
                continue
            else:
                index=i-1
                break
        for j in range(len(nums)-1,index,-1):
            if nums[j]>nums[index]:
                nums[j],nums[index]=nums[index],nums[j]
                break
        nums[index+1:]=nums[index+1:][::-1]
        
        return
a=[2,2,7,5,4,3,2,2,1]
Solution().nextPermutation(a)
print(a)