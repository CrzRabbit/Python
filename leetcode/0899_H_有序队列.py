'''
给出了一个由小写字母组成的字符串 S。然后，我们可以进行任意次数的移动。

在每次移动中，我们选择前 K 个字母中的一个（从左侧开始），将其从原位置移除，并放置在字符串的末尾。

返回我们在任意次数的移动之后可以拥有的按字典顺序排列的最小字符串。

示例 1：
输入：S = "cba", K = 1
输出："acb"
解释：
在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。
在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。

示例 2：
输入：S = "baaca", K = 3
输出："aaabc"
解释：
在第一步中，我们将第一个字符（“b”）移动到最后，获得字符串 “aacab”。
在第二步中，我们将第三个字符（“c”）移动到最后，获得最终结果 “aaabc”。

提示：
1 <= K <= S.length <= 1000
S 只由小写字母组成。
'''
class Solution:
    '''
    k = 1 S为一个环，环状遍历最小串
    k = 2 对于(s[0: i], s[i], s[i + 1], s[i + 1:]):
        s[0: i]依次放到后面变成(s[i], s[i + 1], s[i + 1:], s[0: i])
        s[i + 1]依次放到后面变成(s[i], s[i + 1:], s[0: i], s[i + 1])
        s[i], s[i + 1:]依次放到后面变成(s[0: i], s[i + 1], s[i], s[i + 1:])
    可以交换任意两个相邻的元素，使用冒泡排序
    '''
    def orderlyQueue(self, S, K: int) -> str:
        if K == 1:
            t1 = S
            t2 = S
            for i in range(len(S)):
                t = t1[1:] + t1[0]
                if t2 > t:
                    t2 = t
                t1 = t
            return t2
        if K >= 2:
            st = [i for i in S]
            count = len(st)
            exchange = True
            while count and exchange:
                exchange = False
                for i in range(count - 1):
                    if st[i] > st[i + 1]:
                        st[i], st[i + 1] = st[i + 1], st[i]
                        exchange = True
                count -= 1
            return ''.join(st)
so = Solution()
print(so.orderlyQueue("nhtq", 1))