'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
'''
class Solution:
    def rotate(self, matrix) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                k = len(matrix) - 1 - j
                print(i, j, k, i)
                matrix[i][j], matrix[k][i] = matrix[k][i], matrix[i][j]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
so = Solution()
so.rotate(matrix)
print(matrix)