'''
给定一个正整数 n ，输出外观数列的第 n 项。
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
你可以将其视作是由递归公式定义的数字字符串序列：

countAndSay(1) = "1"
countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。

前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"
'''

'''
递归:
1. n == 1时, 返回‘1’
2. n > 1时, 先获取n-1的外观数列str(n-1), 遍历str(n-1)依次计数格式化为str(n)并返回
'''
class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 0 or n > 30:
            return ''
        if n == 1:
            return '1'
        str = self.countAndSay(n - 1)
        t = str[0]
        count = 1
        ret = ''
        for i in range(1, len(str)):
            if str[i] != t:
                ret += '{0}{1}'.format(count, t)
                t = str[i]
                count = 1
            else:
                count += 1
        ret += '{0}{1}'.format(count, t)
        return ret

so = Solution()
for i in range(1, 11):
    print(so.countAndSay(i))