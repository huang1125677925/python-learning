class Solution:
    def findLength(self, A, B) -> int:
        m, n = len(A), len(B)
        r = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    r[i + 1][j + 1] = r[i][j] + 1
                else:
                    r[i + 1][j + 1] = max(r[i][j + 1], r[i + 1][j])
        
        return r[m][n]
    

print(Solution().findLength([0,0,0,0,0],[0,0,0,0,0]))