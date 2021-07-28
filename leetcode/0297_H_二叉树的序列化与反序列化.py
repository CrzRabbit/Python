'''
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
'''
from leetcode.tools.tree import TreeNode


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