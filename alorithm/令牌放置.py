class Solution:
    def bagOfTokensScore(self, tokens, P: int) -> int:
        count = 0
        tokens.sort()
        l = len(tokens)
        for i in range(l):
            if tokens[i] <= P:
                count += 1
                P = P - tokens[i]
        
        if count == l: return count
        
        p = sum(tokens[-count-1:-1])
        r = 0
        for i in range(l):
            if tokens[i] <= p:
                r += 1
                p -= tokens[i]
        
        return r
    

print(Solution().bagOfTokensScore([100,200],150))