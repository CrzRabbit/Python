'''
给定一个正整数、负整数和 0 组成的 N × M 矩阵，编写代码找出元素总和最大的子矩阵。

返回一个数组 [r1, c1, r2, c2]，其中 r1, c1 分别代表子矩阵左上角的行号和列号，r2, c2 分别代表右下角的行号和列号。若有多个满足条件的子矩阵，返回任意一个均可。

注意：本题相对书上原题稍作改动

示例：
输入：
[
   [-1,0],
   [1,-1]
]
输出：[0,1,0,1]
解释：输入中标粗的元素即为输出所表示的矩阵

说明：
1 <= matrix.length, matrix[0].length <= 200
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        hei = len(matrix)
        wid = len(matrix[0])
        ret = matrix[0][0]
        temp = [0, 0, 0, 0]
        for top in range(hei):
            mem = matrix[top]
            for bottom in range(top, hei):
                if top != bottom:
                    for i in range(wid):
                        mem[i] += matrix[bottom][i]
                cur = mem[0]
                left = 0
                for i in range(wid):
                    if i == 0:
                        cur = mem[0]
                        left = 0
                        right = 0
                    elif cur <= 0:
                        cur = mem[i]
                        left = i
                        right = i
                    else:
                        cur = cur + mem[i]
                        right = i
                    if cur > ret:
                        ret = cur
                        temp = [top, left, bottom, right]
        print(ret)
        return temp

matrix = [[-1,0],
          [1,-1],
          [2, 3]]
Solution().getMaxMatrix(matrix)