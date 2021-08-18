'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
'''
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        ret = 0
        while left <= right:
            print(left, right)
            temp = 0
            if height[left] < height[right]:
                temp = height[left] * (right - left)
                left += 1
            else:
                temp = height[right] * (right - left)
                right -= 1
            if temp > ret:
                ret = temp
        return ret

so = Solution()
print(so.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))