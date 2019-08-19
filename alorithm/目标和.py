class Solution:
    def findTargetSumWays(self, nums, S: int) -> int:
        d = {}
        def dfs(i, cur, d):
            
            if i < len(nums) and (i, cur) not in d: # 搜索周围节点
                d[(i, cur)] = dfs(i + 1, cur + nums[i], d) + dfs(i + 1, cur - nums[i], d)
            print('第几位{0}---和为多少{1}---{2}'.format(i, cur, d))
            return d.get((i, cur), int(cur == S))
        return dfs(0, 0, d)


    


print(Solution().findTargetSumWays([1,1,1,1,1],3))