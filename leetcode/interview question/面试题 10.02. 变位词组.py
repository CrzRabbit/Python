'''
编写一种方法，对字符串数组进行排序，将所有变位词组合在一起。变位词是指字母相同，但排列不同的字符串。

注意：本题相对原题稍作修改

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem = {}
        ret = []
        for s in strs:
            temp = ''.join(sorted(s))
            if temp not in mem:
                mem[temp] = []
                ret.append(mem[temp])
            mem[temp].append(s)
        return ret

Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])