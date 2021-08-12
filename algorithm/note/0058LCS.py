'''
LCS
'''
class LCS:
    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2

    def get(self):
        n = len(self.s1)
        m = len(self.s2)
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        def recursion(n, m):
            if dp[n][m] != -1:
                return dp[n][m]
            if n == -1 or m == -1:
                dp[n][m] = 0
            elif self.s1[n] == self.s2[m]:
                dp[n][m] = 1 + recursion(n - 1, m - 1)
            else:
                dp[n][m] = max(recursion(n - 1, m), recursion(n, m - 1))
            return dp[n][m]
        recursion(n - 1, m - 1)
        return dp[-1][-1]

lcs = LCS('abecbab', 'bdcbabb')
print(lcs.get())