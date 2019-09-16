from collections import Counter


class Solution:
    
    def hasGroupsSizeX(self, deck) -> bool:
        d = Counter(deck)
        
        if len(deck) <= 1:
            return False
        
        res = list(d.values())
        minnum = min(res)
        if minnum == 1:
            return False
        for j in range(2, minnum + 1):
            flag = True
            for i in res:
                if i %j != 0:
                    flag = False
            if flag:
                return True
        return False
    
print(Solution().hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))