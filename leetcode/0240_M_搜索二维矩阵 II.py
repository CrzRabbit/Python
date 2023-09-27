'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

示例 1：

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

示例 2：

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false

提示：

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matrix[i][j] <= 109
每行的所有元素从左到右升序排列
每列的所有元素从上到下升序排列
-109 <= target <= 109
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nl = 0
        ml = 0
        nr = len(matrix) - 1
        mr = len(matrix[0]) - 1
        while nl < nr or ml < mr:
            nmid = (nl + nr) >> 1
            mmid = (ml + mr) >> 1
            if matrix[nmid][mmid] == target:
                return True
            elif matrix[nmid][mmid] > target:
                nr = nmid
                mr = mmid
            else:
                nl = min(nmid + 1, nr)
                ml = min(mmid + 1, mr)
        print(nl, nr, ml, mr)
        if nl == nr:
            l = 0
            r = mr
            while l < r:
                mid = (l + r) >> 1
                if matrix[nl][mid] == target:
                    return True
                elif matrix[nl][mid] > target:
                    r = mid
                else:
                    l = mid + 1
            if l == r and matrix[nl][l] == target:
                return True
        if ml == mr:
            l = 0
            r = nr
            while l < r:
                mid = (l + r) >> 1
                if matrix[mid][ml] == target:
                    return True
                elif matrix[mid][ml] > target:
                    r = mid
                else:
                    l = mid + 1
            if l == r and matrix[l][ml] == target:
                return True
        return False

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]
target = 15
Solution().searchMatrix(matrix, target)