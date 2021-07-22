'''
给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

i - k <= r <= i + k,
j - k <= c <= j + k 且
(r, c) 在矩阵内。


示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]


提示：

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    对于每一个元素，在上下边界之间横向通过前缀和计算
    '''
    @printTime()
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        self.len1 = len(mat)
        self.len2 = len(mat[0])
        ret = [[0 for _ in range(self.len2)] for _ in range(self.len1)]
        temp = mat[0].copy()
        ntop, nbottom, otop, obottom = 0, 0, 0, 0
        for i in range(self.len1):
            ntop = i - k if i - k >= 0 else 0
            nbottom = i + k if i + k <= self.len1 - 1 else self.len1 - 1
            if i == 0:
                for m in range(ntop + 1, nbottom + 1):
                    for n in range(self.len2):
                        temp[n] += mat[m][n]
            else:
                if ntop != otop:
                    for n in range(self.len2):
                        temp[n] -= mat[otop][n]
                if nbottom != obottom:
                    for n in range(self.len2):
                        temp[n] += mat[nbottom][n]
            otop, obottom = ntop, nbottom
            sum = [0 for _ in range(self.len2)]
            sum[0] = temp[0]
            for j in range(1, self.len2):
                sum[j] = temp[j] + sum[j - 1]
            for j in range(self.len2):
                left = j - k if j - k >= 0 else 0
                right = j + k if j + k <= self.len2 - 1 else self.len2 - 1
                if left == 0:
                    ret[i][j] = sum[right]
                else:
                    ret[i][j] = sum[right] - sum[left - 1]
        return ret

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
k = 2
Solution().matrixBlockSum(mat, k)