'''
输入一个字符串，打印出该字符串中字符的所有排列。


你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。


示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

限制：

1 <= s 的长度 <= 8
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def permutation(self, s: str) -> List[str]:
        self.len = len(s)
        list = [s[i] for i in range(self.len)]
        ret = []
        def re(s, list):
            if len(list) == 1:
                ret.append(s + list[0])
            temp = []
            for i in range(len(list)):
                if list[i] not in temp:
                    temp.append(list[i])
                    re(s + list[i], list[:i] + list[i + 1:])
        re('', list)
        return ret

Solution().permutation('aab')