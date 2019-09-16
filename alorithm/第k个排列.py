class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def pailie(nums, count, res, path):
            if count[0] == k:
                res.append(''.join(path))
                return
            if nums == []:
                count[0] += 1
                return
            
            for i in range(len(nums)):
                pailie(nums[:i] + nums[i + 1:], count, res, path + [str(nums[i])])
        
        res = []
        count = [0]
        pailie(list(range(1, n + 1)), count, res, [])
        return res[0]
    


class Solution1:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0:
            return []
        nums = [i + 1 for i in range(n)]
        used = [False for _ in range(n)]
        
        self.__dfs(nums, used, n, k, 0, [])
    
    
    def __factorial(self, n):
        # 这种编码方式包括了 0 的阶乘是 1 这种情况
        res = 1
        while n:
            res *= n
            n -= 1
        return res
    
    
    def __dfs(self, nums, used, n, k, depth, pre):
        if depth == n:
            # 在叶子结点处结算
            print(''.join(pre))
            return
        # 后面的数的全排列的个数
        ps = self.__factorial(n - 1 - depth)
        for i in range(n):
            # 如果这个数用过，就不再考虑
            if used[i]:
                continue
            # 后面的数的全排列的个数小于 k 的时候，执行剪枝操作
            # if ps < k:
            #     k -= ps
            #     continue
            pre.append(str(nums[i]))
            # 因为直接走到叶子结点，因此状态不用恢复
            used[i] = True
            self.__dfs(nums, used, n, k, depth + 1, pre)
            pre.pop()
            used[i]=False
            
    

print(Solution1().getPermutation(4,3))