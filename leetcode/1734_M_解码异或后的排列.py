'''
给你一个整数数组 perm ，它是前 n 个正整数的排列，且 n 是个 奇数 。

它被加密成另一个长度为 n - 1 的整数数组 encoded ，满足 encoded[i] = perm[i] XOR perm[i + 1] 。比方说，如果 perm = [1,3,2] ，那么 encoded = [2,1] 。

给你 encoded 数组，请你返回原始数组 perm 。题目保证答案存在且唯一。

示例 1：
输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]

示例 2：
输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]
 

提示：
3 <= n < 105
n 是奇数。
encoded.length == n - 1
'''
from typing import List


class Solution:
    '''
    encoded[1] = arr[1] ^ arr[2]
    encoded[3] = arr[3] ^ arr[4]
    arr[0] = (1 ^ 2 ^...^n) ^ (encoded[1] ^ encoded[3] ^ encoded[5] ^ ... ^ encoded[n - 1])
    '''
    def decode(self, encoded: List[int]) -> List[int]:
        ret = []
        nxor = 1
        for i in range(2, len(encoded) + 2):
            nxor ^= i

        for i in range(1, len(encoded), 2):
            nxor ^= encoded[i]

        ret.append(nxor)
        for en in encoded:
            nxor ^= en
            ret.append(nxor)
        return ret

print()
nums = [6,5,4,6]
so = Solution()
print(so.decode(nums))
