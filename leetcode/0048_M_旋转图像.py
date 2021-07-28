'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''
from leetcode.tools.tool import printMatrix


class Solution:
    '''
    从外到内，按圈旋转90度交换
    '''
    def rotate(self, matrix) -> None:
        rows = len(matrix) - 1
        columns = len(matrix[0]) - 1
        for i in range(int(len(matrix) / 2)):
            for j in range(i, columns - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[rows - j][i]
                matrix[rows - j][i] = matrix[rows - i][columns - j]
                matrix[rows - i][columns - j] = matrix[j][columns - i]
                matrix[j][columns - i] = temp

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
so = Solution()
printMatrix(matrix)
so.rotate(matrix)
printMatrix(matrix)