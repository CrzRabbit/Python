'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
'''
from leetcode.tools.tree import *
class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
    #     ret = []
    #     nodes = []
    #     if root == None:
    #         return ret
    #     else:
    #         nodes.append(root)
    #     flag = True
    #     while nodes.__len__():
    #         temp_nodes = []
    #         temp_ret = []
    #         for i in range(nodes.__len__()):
    #             if nodes[i] != None:
    #                 temp_ret.append(nodes[i].val)
    #             if flag:
    #                 if nodes[i].left != None:
    #                     temp_nodes.append(nodes[i].left)
    #                 if nodes[i].right != None:
    #                     temp_nodes.append(nodes[i].right)
    #             else:
    #                 if nodes[i].right != None:
    #                     temp_nodes.append(nodes[i].right)
    #                 if nodes[i].left != None:
    #                     temp_nodes.append(nodes[i].left)
    #         ret.append(temp_ret)
    #         temp_nodes.reverse()
    #         nodes = temp_nodes
    #         flag = not flag
    #     return ret
        ret = []
        nodes = []
        if root == None:
            return ret
        else:
            nodes.append(root)
        flag = False
        while nodes.__len__():
            temp_nodes = []
            temp_ret = []
            for i in range(nodes.__len__()):
                if nodes[i]:
                    temp_ret.append(nodes[i].val)
                if nodes[i].left:
                    temp_nodes.append(nodes[i].left)
                if nodes[i].right:
                    temp_nodes.append(nodes[i].right)
            if flag:
                temp_ret.reverse()
            flag = not flag
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
so = Solution()
print(so.zigzagLevelOrder(n0))