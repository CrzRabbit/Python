'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"

示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。

提示：

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        ret = ''
        i = 0
        j = 0
        while True:
            j = 0
            if len(strs) > 0:
                if i >= len(strs[0]):
                    return ret
                else:
                    ret += strs[0][i:i + 1]
            else:
                break
            while j < len(strs):
                if i > len(strs[j]) or ret != strs[j][0:i + 1]:
                    return ret[:-1]
                j += 1
            i += 1
        return ret

so = Solution()
print(so.longestCommonPrefix([]))