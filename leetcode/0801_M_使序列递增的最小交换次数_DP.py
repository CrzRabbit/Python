'''
我们有两个长度相等且不为空的整型数组 A 和 B 。

我们可以交换 A[i] 和 B[i] 的元素。注意这两个元素在各自的序列中应该处于相同的位置。

在交换过一些元素之后，数组 A 和 B 都应该是严格递增的（数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.length - 1]）。

给定数组 A 和 B ，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。

示例:
输入: A = [1,3,5,4], B = [1,2,3,7]
输出: 1
解释:
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。

注意:
A, B 两个数组的长度总是相等的，且长度的范围为 [1, 1000]。
A[i], B[i] 均为 [0, 2000]区间内的整数。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    '''
    DP
    '''
    @printTime()
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        self.len = len(nums1)
        '''
        nex表示第i组不交换的情况下0 ~ i保持递增总共需要的最小交换次数，i = 0，nex = 0
        ex表示第i组交换的情况下0 ~ i保持递增总共需要的最小交换次数，i = 0，ex = 1
        1. 如果nums1[i] > nums1[i - 1], nums1[i] > nums2[i - 1]
        nums2[i] > nums2[i - 1], nums2[i] > nums1[i - 1]
        那么第i组交不交换都可以: ex(i) = min(ex(i - 1), nex(i - 1)) + 1
        nex(i) = min(ex(i - 1), nex(i - 1))
        2. 如果只满足nums1[i] > nums1[i - 1], nums1[i] > nums2[i - 1]
        不满足nums2[i] > nums2[i - 1], nums2[i] > nums1[i - 1]
        那么第i - 1交换，第i也得交换: ex(i) = ex(i - 1) + 1
        第i - 1不交换，第i也不能交换: nex(i) = nex(i - 1)
        3. 都不满足的情况下
        那么第i - 1交换，第i就不能交换: ex(i) = nex(i - 1) + 1
        第i - 1不交换，第i必须交换: nex(i) = ex(i - 1)
        '''
        nex = 0
        ex = 1
        for i in range(1, self.len):
            cond1 = nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]
            cond2 = nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]
            t1 = nex
            t2 = ex
            if cond1 and cond2:
                nex = min(t1, t2)
                ex = min(t1, t2) + 1
            elif cond1:
                ex = t2 + 1
            else:
                nex = t2
                ex = t1 + 1
        return min(ex, nex)

A = [0,4,4,5,9]
B = [0,1,6,8,10]
Solution().minSwap(A, B)
# 0 0 1 1 1
# 1 1 1 2 2