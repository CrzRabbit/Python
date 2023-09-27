'''
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

找到所有长度为 n 的中心对称数。

示例 :

输入:  n = 2
输出: ["11","69","88","96"]
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def findStrobogrammatic(self, n: int) -> List[str]:
        ret = []
        dic = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}

        return ret
Solution().findStrobogrammatic(4)