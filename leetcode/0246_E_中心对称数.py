'''
中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。

请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。


示例 1:

输入: num = "69"
输出: true

示例 2:

输入: num = "88"
输出: true

示例 3:

输入: num = "962"
输出: false

示例 4：

输入：num = "1"
输出：true
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def isStrobogrammatic(self, num: str) -> bool:
        dic = {'0': '0', '1': '1', '6': '9', '9': '6', '8': '8'}
        for i in range((len(num) + 1) >> 1):
            if num[i] not in dic or dic[num[i]] != num[len(num) - 1 - i]:
                return False
        return True

num = "2"
Solution().isStrobogrammatic(num)