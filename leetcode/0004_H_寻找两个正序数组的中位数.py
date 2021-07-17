'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000

提示：
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        k = int((len(nums1) + len(nums2) + 1) / 2)
        l = len(nums1) + len(nums2)
        print(k, nums1, nums2)
        while k > 1:
            t = int(k / 2)
            if len(nums1) == 0:
                nums2 = nums2[k - 1:]
                break
            if len(nums2) == 0:
                nums1 = nums1[k - 1:]
                break
            if len(nums1) < t:
                if nums1[len(nums1) - 1] <= nums2[t - 1]:
                    k -= len(nums1)
                    nums1 = nums1[len(nums1):]
                else:
                    k -= t
                    nums2 = nums2[t:]
            elif len(nums2) < t:
                if nums2[len(nums2) - 1] <= nums1[t - 1]:
                    k -= len(nums2)
                    nums2 = nums2[len(nums2):]
                else:
                    k -= t
                    nums1 = nums1[t:]
            else:
                if nums1[t - 1] <= nums2[t - 1]:
                    nums1 = nums1[t:]
                else:
                    nums2 = nums2[t:]
                k -= t
            print(k, nums1, nums2)
        print(k, nums1, nums2)
        if l % 2 == 1:
            if len(nums1) == 0:
                return nums2[0]
            elif len(nums2) == 0:
                return nums1[0]
            else:
                if nums1[0] < nums2[0]:
                    return nums1[0]
                else:
                    return nums2[0]
        elif l % 2 == 0:
            if len(nums1) == 0:
                return (nums2[0] + nums2[1]) / 2
            elif len(nums2) == 0:
                return (nums1[0] + nums1[1]) / 2
            else:
                i = 0
                j = 0
                k = 0
                sum = 0
                while k < 2:
                    if j >= len(nums2) or (i < len(nums1) and nums1[i] <= nums2[j]):
                        sum += nums1[i]
                        i += 1
                    else:
                        sum += nums2[j]
                        j += 1
                    k += 1
                return sum / 2
        return 0

so = Solution()
print(so.findMedianSortedArrays([], [2, 3]))