class Solution:
    def PredictTheWinner(self, nums):
        n = len(nums)
        if n % 2 == 0 or n == 1:
            return True
        dp = [[0] * n for _ in range(n)]
        for i in reversed(range(n)):
            for j in range(i + 1, n):
                print(i,j)
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        for item in dp:
            print(item)


# Solution().PredictTheWinner([1,5,233,7])
def PredictTheWinner(nums):
    n = len(nums)
    return helper(nums, 0, n - 1)

def helper(nums,i,j):
    if i==j:
        return nums[i]

    left = nums[i] - helper(nums, i + 1, j)
    
    right = nums[j] - helper(nums, i, j - 1)
    
    return max(left, right)

print(PredictTheWinner([5,233,7]))
