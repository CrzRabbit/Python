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