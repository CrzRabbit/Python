'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
'''
from leetcode.tools.tree import *
class Solution:
    def levelOrder(self, root: TreeNode):
        ret = []
        nodes = []
        if root == None:
            return ret
        else:
            nodes.append(root)
        while nodes.__len__():
            temp_nodes = []
            temp_ret = []
            for i in range(nodes.__len__()):
                if nodes[i] != None:
                    temp_ret.append(nodes[i].val)
                if nodes[i].left != None:
                    temp_nodes.append(nodes[i].left)
                if nodes[i].right != None:
                    temp_nodes.append(nodes[i].right)
            ret.append(temp_ret)
            nodes = temp_nodes
        return ret

n0 = TreeNode(0)
n1 = TreeNode(1)
n0.left = n1
n2 = TreeNode(2)
n0.right = n2
n3 = TreeNode(3)
n2.left = n3
so = Solution()
showTree(n0)
print(so.levelOrder(n0))