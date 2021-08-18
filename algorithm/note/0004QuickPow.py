'''
快速幂
'''
class QPow:
    '''
    递归快速幂
    '''
    def qpow(self, a, n):
        if n == 0:
            return 1
        elif n % 2 == 1:
            return a * self.qpow(a, n - 1)
        else:
            temp = self.qpow(a, n // 2)
            return temp ** 2
    '''
    位运算快速幂
    '''
    def qpow2(self, a, n):
        ans = 1
        while n:
            if n & 1:
                ans *= a
            a *= a
            n >>= 1
        return ans
    '''
    矩阵快速幂
    '''
    def pmatrix(self, a, b):
        ret = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
        for i in range(len(ret)):
            for j in range(len(ret[0])):
                s = 0
                for k in range(len(a[0])):
                    s += a[i][k] * b[k][j]
                ret[i][j] = s
        return ret

    def qpow3(self, mat, n, base):
        ans = [[0 for _ in range(len(mat))] for _ in range(len(mat))]
        for i in range(len(mat)):
            ans[i][i] = 1
        while n:
            if n & 1:
                ans = self.pmatrix(ans, mat)
            mat = self.pmatrix(mat, mat)
            n >>= 1
        return self.pmatrix(ans, base)