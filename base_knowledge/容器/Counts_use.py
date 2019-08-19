from collections import Counter


s = 'huangchuanghuanghuangckk'

s = list(s)

r=Counter(s)


colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(s)
d=dict(sorted(favs.items(),key=lambda x:(-x[1],x[0])))
print(d)

print(sorted(['l','c']))


class Solution:
    def maxProduct(self, nums) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums) ):
            dp[i] = max([dp[i - 1] * nums[i], nums[i], nums[i] * nums[i - 1]])
        
        return max(dp)
 
print(Solution().maxProduct([-2,3,-4]))

