from leetcode.tools.tree import *
from leetcode.tools.time import *
class Solution:
    def buildTree(self, inorder, postorder) -> TreeNode:
        def getLeftRight(inorder, postorder):
            for i in range(inorder.__len__()):
                if inorder[i] == postorder[postorder.__len__() - 1]:
                    return postorder[0: i], postorder[i:postorder.__len__() - 1], inorder[0: i], inorder[i + 1:]
            return [], [], [], []
        root = None
        if postorder.__len__() and inorder.__len__() and postorder.__len__() == inorder.__len__():
            root = TreeNode()
            root.val = postorder[postorder.__len__() - 1]
            pre_left, pre_right, in_left, in_right = getLeftRight(inorder, postorder)
            if pre_left.__len__() == 0:
                root.left = None
            elif pre_left.__len__() == 1:
                root.left = TreeNode(pre_left[pre_left.__len__() - 1])
            else:
                root.left = self.buildTree(in_left, pre_left)
            if pre_right.__len__() == 0:
                root.right = None
            elif pre_right.__len__() == 1:
                root.right = TreeNode(pre_right[pre_right.__len__() - 1])
            else:
                root.right = self.buildTree(in_right, pre_right)
        return root

so = Solution()
print_time()
showTree(so.buildTree([9,3,15,20,7], [9,15,7,20,3]))
print_time()