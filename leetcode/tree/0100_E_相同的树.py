'''
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
'''
from leetcode.tools.tree import *
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        showTree(p)
        showTree(q)
        left = []
        right = []
        def isNodeSame(p, q):
            if (p and q and p.val == q.val) or (p == None and q == None):
                return True
            return False
        if isNodeSame(p, q):
            left.append(p)
            right.append(q)
        else:
            return False
        while left.__len__() and right.__len__():
            if left.__len__() != right.__len__():
                return False
            temp_left = []
            temp_right = []
            for i in range(0, left.__len__()):
                if left[i] == None or right[i] == None:
                    continue
                if isNodeSame(left[i].left, right[i].left):
                    temp_left.append(left[i].left)
                    temp_right.append(right[i].left)
                else:
                    return False
                if isNodeSame(left[i].right, right[i].right):
                    temp_left.append(left[i].right)
                    temp_right.append(right[i].right)
                else:
                    return False
            left = temp_left
            right = temp_right
        return True

n0 = TreeNode(0)
n1 = TreeNode(1)
n0.left = n1
n2 = TreeNode(2)
n0.right = n2
n3 = TreeNode(3)
n2.left = n3
so = Solution()
print(so.isSameTree(n0, n0))