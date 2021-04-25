'''
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。
'''
from leetcode.tools.tree import *
from leetcode.tools.time import *
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        def getLeftRight(preorder, inorder):
            for i in range(inorder.__len__()):
                if inorder[i] == preorder[0]:
                    return preorder[1: i + 1], preorder[i + 1:], inorder[0: i], inorder[i + 1:]
            return [], [], [], []
        root = None
        if preorder.__len__() and inorder.__len__() and preorder.__len__() == inorder.__len__():
            root = TreeNode()
            root.val = preorder[0]
            pre_left, pre_right, in_left, in_right = getLeftRight(preorder, inorder)
            if pre_left.__len__() == 0:
                root.left = None
            elif pre_left.__len__() == 1:
                root.left = TreeNode(pre_left[0])
            else:
                root.left = self.buildTree(pre_left, in_left)
            if pre_right.__len__() == 0:
                root.right = None
            elif pre_right.__len__() == 1:
                root.right = TreeNode(pre_right[0])
            else:
                root.right = self.buildTree(pre_right, in_right)
        return root

so = Solution()
print_time()
showTree(so.buildTree([3,9,20,15,7], [9,3,15,20,7]))
print_time()