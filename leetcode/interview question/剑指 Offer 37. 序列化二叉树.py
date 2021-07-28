'''
请实现两个函数，分别用来序列化和反序列化二叉树。

你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
'''
import datetime


from leetcode.tools.tree import buildTree, showTree, TreeNode


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        str = ''
        if root is None:
            return str
        nodes = [root]
        while nodes.__len__():
            temp = []
            count = 0
            for node in nodes:
                if node:
                    str += '{} '.format(node.val)
                    temp.append(node.left)
                    temp.append(node.right)
                    if node.left:
                        count += 1
                    if node.right:
                        count += 1
                else:
                    str += ' '
            if count:
                nodes = temp
            else:
                break
        return str

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')[:-1]
        self.len = len(data)
        if self.len == 0:
            return None
        root = TreeNode(data[0])
        nodes = [root]
        i = 1
        while len(nodes) and i < self.len:
            temp = []
            for t in nodes:
                if t:
                    if i < self.len:
                        node = None
                        if data[i].__len__():
                            node = TreeNode(data[i])
                            t.left = node
                        i += 1
                        temp.append(node)
                    if i < self.len:
                        node = None
                        if data[i].__len__():
                            node = TreeNode(data[i])
                            t.right = node
                        i += 1
                        temp.append(node)
            nodes = temp
        return root


# Your Codec object will be instantiated and called as such:
data = ''
for i in range(20):
    data += '{} '.format(i)
    data += ' '
codec = Codec()
root = codec.deserialize(data)
showTree(root)
start = datetime.datetime.now()
print(start)
# showTree(codec.deserialize(codec.serialize(root)), 3)
codec.deserialize(codec.serialize(root))
end = datetime.datetime.now()
print(end)
print(end - start)
