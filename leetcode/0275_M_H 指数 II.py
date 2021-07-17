'''
给定一位研究者论文被引用次数的数组（被引用次数是非负整数），数组已经按照 升序排列 。编写一个方法，计算出研究者的 h 指数。

h 指数的定义: “h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （N 篇论文中）总共有 h 篇论文分别被引用了至少 h 次。（其余的 N - h 篇论文每篇被引用次数不多于 h 次。）"


示例:

输入: citations = [0,1,3,5,6]
输出: 3
解释: 给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
     由于研究者有 3 篇论文每篇至少被引用了 3 次，其余两篇论文每篇被引用不多于 3 次，所以她的 h 指数是 3。

说明:

如果 h 有多有种可能的值 ，h 指数是其中最大的那个。


进阶：

这是 H 指数 的延伸题目，本题中的 citations 数组是保证有序的。
你可以优化你的算法到对数时间复杂度吗？
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def hIndex(self, citations: List[int]) -> int:
        len1 = len(citations)
        left = 0
        right = len1 - 1
        while left + 1 < right:
            mid = (left + right + 1) >> 1
            if citations[mid] < len1 - mid:
                left = mid
            elif citations[mid] > len1 - mid:
                right = mid
            else:
                return len1 - mid
        return max(min(citations[left], len1 - left), min(citations[right], len1 - right))

#citations = [0,3,3,5,8,13,14,14,17,24,27,28,30,31,32,34,40,41,41,41,44,46,48,60,61,69,70,73,74,77,80,80,84,96,101,108,121,122,124,129,132,132,133,134,139,140,144,147,147,147,147,150,151,151,154,157,169,169,170,172,178,193,194,195,200,201,202,202,203,212,213,224,224,224,229,231,231,233,237,239,241,244,244,250]
citations = [0,3]
Solution().hIndex(citations)