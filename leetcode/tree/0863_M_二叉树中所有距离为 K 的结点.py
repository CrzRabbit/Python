'''
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。



示例 1：

输入：root = [3,5,1,6,2,0,8,None,None,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1

注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。


提示：

给定的树是非空的。
树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
目标结点 target 是树上的结点。
0 <= K <= 1000.
'''
from typing import List

from leetcode.tools.time import printTime
from leetcode.tools.tree import TreeNode, buildLTree


class Solution:
    @printTime()
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ret = []
        nodes = [root]
        index = 0
        found = False
        while nodes.__len__() and not found:
            temp = []
            print(index)
            for i in range(index, len(nodes)):
                if nodes[i]:
                    if nodes[i].val == target.val:
                        found = True
                        index = i
                        break
                    temp.append(nodes[i].left)
                    temp.append(nodes[i].right)
                else:
                    temp.append(None)
                    temp.append(None)
            if not found:
                nodes += temp
                index = index * 2 + 1
        def getKNodes(node, t):
            nodes = [node]
            for i in range(t):
                temp = []
                for node in nodes:
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                nodes = temp
            for node in nodes:
                ret.append(node.val)
        lastindex = index
        while index >= 0 and k >= 0:
            if k == 0:
                ret.append(nodes[index].val)
            else:
                if nodes[index].left and (lastindex == index or lastindex % 2 == 0):
                    getKNodes(nodes[index].left, k - 1)
                if nodes[index].right and (lastindex == index or lastindex % 2 == 1):
                    getKNodes(nodes[index].right, k - 1)
            lastindex = index
            index = (index - 1) // 2
            k -= 1
        return ret

root = [0,1,29,2,3,41,43,11,4,None,5,None,None,None,None,27,15,18,7,19,6,None,36,None,33,None,None,8,10,None,22,None,17,None,None,None,None,16,9,20,12,23,28,None,39,34,None,14,None,46,42,26,13,31,None,30,48,None,None,None,None,None,37,None,47,None,None,45,None,21,44,None,None,None,35,None,49,None,None,None,None,None,None,24,32,None,None,None,None,None,None,25,None,None,None,None,38,None,40]
Solution().distanceK(buildLTree(root), TreeNode(37), 17)