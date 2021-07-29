'''

在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。


给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。



示例 1：

输入：label = 14
输出：[1,3,4,14]

示例 2：

输入：label = 26
输出：[1,2,6,10,26]


提示：

1 <= label <= 10^6
'''
from typing import List

from leetcode.tools.time import printTime


class Solution:
    @printTime()
    def pathInZigZagTree(self, label: int) -> List[int]:
        ret = []
        index = 0
        for i in range(32):
            if 2 ** i <= label < 2 ** (i + 1):
                index = i
                break
        while label >= 1 and index >= 0:
            ret.append(label)
            if index % 2 == 1:
                label = (2 ** (index + 1) - 1) - (label - 2 ** index)
                if label % 2 == 0:
                    label //= 2
                else:
                    label = (label - 1) // 2
            else:
                if label % 2 == 0:
                    label //= 2
                else:
                    label = (label - 1) // 2
                label = 2 ** index - 1 - (label - 2 ** (index - 1))
            index -= 1
        ret.reverse()
        return ret

Solution().pathInZigZagTree(16)