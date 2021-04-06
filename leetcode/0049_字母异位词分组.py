'''
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
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
class Solution:
    def _groupAnagrams(self, strs):
        ret = []
        ret_dict = []
        def getDict(str):
            sdict = dict()
            for s in str:
                if sdict.keys().__contains__(s):
                    sdict[s] += 1
                else:
                    sdict[s] = 1
            return sdict
        def isGroupAnagrams(d1, d2):
            if len(d1) == len(d2):
                for key in d1.keys():
                    if not d2.keys().__contains__(key) or d1[key] != d2[key]:
                        return False
                return True
            return False
        for s in strs:
            found = False
            d = getDict(s)
            for i in range(len(ret_dict)):
                if isGroupAnagrams(ret_dict[i], d):
                    ret[i].append(s)
                    found = True
            if not found:
                ret_dict.append(d)
                l = list()
                l.append(s)
                ret.append(l)
        return ret
    def groupAnagrams(self, strs):
        ret = dict()
        magic = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        for str in strs:
            num = 1
            for s in str:
                num *= magic[ord(s) - 97]
            if ret.keys().__contains__(num):
                ret[num].append(str)
            else:
                l = []
                l.append(str)
                ret[num] = l
        return list(ret.values())

so = Solution()
print(so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))