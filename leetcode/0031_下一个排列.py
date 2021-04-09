'''
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。
'''

'''
1. 从后往前从[left, right]查找相邻元素组成的升序对(i, j), 此时[j, right]降序
2. 从后往前从[j, right]查找第一个大于nums[i]的元素与nums[i]进行交换, 此时[j, right]降序
3. 对[j, right]升序排序
'''
class Solution:
    def nextPermutation(self, nums) -> None:
        def next(left, right):
            found = False
            if right - left <= 1:
                return
            r = right - 1
            while r > left:
                if nums[r] > nums[r - 1]:
                    r1 = right - 1
                    while r1 > r - 1:
                        if nums[r1] > nums[r - 1]:
                            found = True
                            nums[r - 1] = nums[r - 1] ^ nums[r1]
                            nums[r1] = nums[r - 1] ^ nums[r1]
                            nums[r - 1] = nums[r - 1] ^ nums[r1]
                            left = r
                            break
                        r1 -= 1
                if found:
                    break
                r -= 1
            exchange = True
            while right > left and exchange:
                exchange = False
                for j in range(left, right - 1):
                    if nums[j] > nums[j + 1]:
                        exchange = True
                        nums[j] = nums[j] ^ nums[j + 1]
                        nums[j + 1] = nums[j] ^ nums[j + 1]
                        nums[j] = nums[j] ^ nums[j + 1]
                right -= 1
        next(0, len(nums))

nums = [1,3,2]
so = Solution()
so.nextPermutation(nums)
print(nums)