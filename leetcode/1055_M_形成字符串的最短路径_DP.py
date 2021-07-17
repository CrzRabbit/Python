'''
对于任何字符串，我们可以通过删除其中一些字符（也可能不删除）来构造该字符串的子序列。

给定源字符串 source 和目标字符串 target，找出源字符串中能通过串联形成目标字符串的子序列的最小数量。如果无法通过串联源字符串中的子序列来构造目标字符串，则返回 -1。
'''
from leetcode.tools.time import printTime


class Solution:
    '''
    遍历target，然后在source中查找
    '''
    @printTime()
    def shortestWay(self, source: str, target: str) -> int:
        ret = 1
        count = 0
        self.slen = len(source)
        self.tlen = len(target)
        for i in range(len(target)):
            if source[count] != target[i]:
                temp = count
                while source[count] != target[i]:
                    count += 1
                    if count == self.slen:
                        count = 0
                        ret += 1
                    if count == temp:
                        return -1
            count += 1
            if count == self.slen and i != self.tlen - 1:
                count = 0
                ret += 1
        return ret

    '''
    DP
    '''
    @printTime()
    def _1shortestWay(self, source: str, target: str) -> int:
        self.tlen = target.__len__()
        self.slen = source.__len__()
        dp = [-1 for i in range(len(target))]
        count = 0
        if source.__contains__(target[0]):
            dp[0] = 1
            count = source.find(target[0])
            count += 1
        else:
            return -1
        for i in range(1, len(target)):
            print(i, count)
            if source[count:].__contains__(target[i]):
                dp[i] = dp[i - 1]
                count = source[count:].find(target[i]) + count
            elif source[:count].__contains__(target[i]):
                dp[i] = dp[i - 1] + 1
                count = source[:count].find(target[i])
            else:
                return -1
            count += 1
        return dp[-1]

source = "abc"
target = "abcbc"
Solution().shortestWay(source, target)
Solution()._1shortestWay(source, target)