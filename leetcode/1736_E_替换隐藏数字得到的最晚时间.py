'''
给你一个字符串 time ，格式为 hh:mm（小时：分钟），其中某几位数字被隐藏（用 ? 表示）。

有效的时间为 00:00 到 23:59 之间的所有时间，包括 00:00 和 23:59 。

替换 time 中隐藏的数字，返回你可以得到的最晚有效时间。


示例 1：

输入：time = "2?:?0"
输出："23:50"
解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。
示例 2：

输入：time = "0?:3?"
输出："09:39"
示例 3：

输入：time = "1?:22"
输出："19:22"

提示：

time 的格式为 hh:mm
题目数据保证你可以由输入的字符串生成有效的时间
'''
from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def maximumTime(self, time: str) -> str:
        ret = []
        if time[0] == '?':
            if '0' <= time[1] <= '3' or time[1] == '?':
                ret.append('2')
            else:
                ret.append('1')
        else:
            ret.append(time[0])
        if time[1] == '?':
            if ret[0] == '0' or ret[0] == '1':
                ret.append('9')
            else:
                ret.append('3')
        else:
            ret.append(time[1])
        ret.append(':')
        if time[3] == '?':
            ret.append('5')
        else:
            ret.append(time[3])
        if time[4] == '?':
            ret.append('9')
        else:
            ret.append(time[4])
        return ''.join(ret)

Solution().maximumTime("0?:3?")