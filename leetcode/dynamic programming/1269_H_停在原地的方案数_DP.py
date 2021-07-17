'''
有一个长度为 arrLen 的数组，开始有一个指针在索引 0 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数 steps 和 arrLen ，请你计算并返回：在恰好执行 steps 次操作以后，指针仍然指向索引 0 处的方案数。

由于答案可能会很大，请返回方案数 模 10^9 + 7 后的结果。

示例 1：
输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动

示例  2：
输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动

示例 3：
输入：steps = 4, arrLen = 2
输出：8

提示：
1 <= steps <= 500
1 <= arrLen <= 10^6
'''
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        ret = [[0, 0, 0]]
        for i in range(steps):
            temp = []
            for r in ret:
                left = r[0]
                right = r[1]
                hold = r[2]
                if int((steps - hold) / 2) > right and (right - left) < arrLen - 1:
                    temp.append([left, right + 1, hold])
                if (steps - right * 2) > hold:
                    temp.append([left, right, hold + 1])
                if left < right and (right - left) > 0:
                    temp.append([left + 1, right, hold])
            ret = temp
        return len(ret)
    '''
    动态规划, ret[0][0] = 1 ret[0][j] = 0
    ret[i][j] = ret[i - 1][j] + ret[i - 1][j - 1] + ret[i - 1][j + 1]
    '''
    def _numWays(self, steps: int, arrLen: int) -> int:
        if arrLen > steps:
            arrLen = steps + 1
        ret = [[0 for i in range(arrLen)] for i in range(steps + 1)]
        ret[0][0] = 1
        for i in range(1, steps + 1):
            for j in range(arrLen):
                ret[i][j] = ret[i - 1][j] % (10 ** 9 + 7)
                if j > 0:
                    ret[i][j] += ret[i - 1][j - 1] % (10 ** 9 + 7)
                if j < arrLen - 1:
                    ret[i][j] += ret[i - 1][j + 1] % (10 ** 9 + 7)
        return ret[steps][0] % (10 ** 9 + 7)

steps = 430
arrLen = 148488
so = Solution()
#print(so.numWays(steps, arrLen))
print(so._numWays(steps, arrLen))