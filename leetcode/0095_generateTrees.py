from leetcode.tools.tree import *
class Solution:
    def generateTrees(self, n: int):
        nodes = []
        def genTree(x, y):
            nodes = []
            if x == y:
                node = TreeNode(x)
                nodes.append(node)
                return nodes
            if x > y:
                nodes.append(None)
                return nodes
            for i in range(x, y + 1):
                node = TreeNode(i)
                left_trees = genTree(x, i - 1)
                right_trees = genTree(i + 1, y)
                for l in left_trees:
                    node.left = l
                    for r in right_trees:
                        node.right = r
                        temp_node = TreeNode(node.val, node.left, node.right)
                        nodes.append(temp_node)
            return nodes
        return genTree(1, n)

so = Solution()
nodes = so.generateTrees(7)
print(nodes.__len__())
for node in nodes:
    showTree(node)