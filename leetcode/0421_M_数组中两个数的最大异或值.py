'''
给你一个整数数组 nums ，返回 nums[i] XOR nums[j] 的最大运算结果，其中 0 ≤ i ≤ j < n 。

进阶：你可以在 O(n) 的时间解决这个问题吗？

示例 1：
输入：nums = [3,10,5,25,2,8]
输出：28
解释：最大运算结果是 5 XOR 25 = 28.

示例 2：
输入：nums = [0]
输出：0

示例 3：
输入：nums = [2,4]
输出：6

示例 4：
输入：nums = [8,10,2]
输出：10

示例 5：
输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
输出：127

提示：
1 <= nums.length <= 2 * 104
0 <= nums[i] <= 231 - 1
'''
from typing import List

class Trie:
    def __init__(self):
        self.children = [None for i in range(2)]
        self.isEnd = False

    def insert(self, str):
        node = self
        for s in str:
            index = ord(s) - ord('0')
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.isEnd = True

    def search(self, str):
        node = self
        ret = 0
        for s in str:
            index = ord(s) - ord('0')
            rindex = 0 if index else 1
            if node.children[rindex]:
                ret = ret << 1
                ret += 1
                node = node.children[rindex]
            elif node.children[index]:
                ret = ret << 1
                node = node.children[index]
            else:
                return 0
        return ret

class Solution:
    '''
    前缀树（Trie）
    '''
    def findMaximumXOR(self, nums: List[int]) -> int:
        def toBinStr(num):
            bit = 30
            str = ""
            while bit >= 0:
                str += '{}'.format(1 if num & 2**bit else 0)
                bit -= 1
            return str
        trie = Trie()
        ret = 0
        for num in nums:
            str = toBinStr(num)
            temp = trie.search(str)
            if temp > ret:
                ret = temp
            trie.insert(str)
        return ret

nums = [2,4]
so = Solution()
print(so.findMaximumXOR(nums))