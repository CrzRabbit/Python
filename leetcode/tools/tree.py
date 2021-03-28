class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def morrisTraverse(root):
    temp = None
    vals = []
    while root:
        if root.left:
            temp = root.left
            while temp.right and temp.right is not root:
                temp = temp.right
            if temp.right is None:
                temp.right = root
                root = root.left
            else:
                temp.right = None
                vals.append(root.val)
                root = root.right
        else:
            vals.append(root.val)
            root = root.right
    print(vals)

def constructMaximumBinaryTree(nums) -> TreeNode:
    if nums.__len__() == 0:
        return None
    def getTree(nums, left, right):
        if left == right:
            return None
        index = left
        for i in range(left + 1, right):
            if nums[i] > nums[index]:
                index = i
        node = TreeNode(nums[index])
        node.left = getTree(nums, left, index)
        node.right = getTree(nums, index + 1, right)
        return node
    return getTree(nums, 0, nums.__len__())

def isBalanced(self, root: TreeNode) -> bool:
    if not root:
        return True
    def getDepth(node):
        if not node:
            return 0, True
        else:
            left_depth, left_balance = getDepth(node.left)
            right_depth, right_balance = getDepth(node.right)
            flag = True
            if left_depth - right_depth > 1 or left_depth - right_depth < -1 or not left_balance or not right_balance:
                flag = False
            if left_depth >= right_depth:
                return left_depth + 1, flag
            else:
                return right_depth + 1, flag
    left_depth, left_balance = getDepth(root.left)
    right_depth, right_balance = getDepth(root.right)
    if (left_depth - right_depth > 1 or left_depth - right_depth < -1) or not left_balance or not right_balance:
        return False
    else:
        return True

def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
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

def recoverTree(root: TreeNode) -> None:
    def inorderTraversal(root: TreeNode):
        ret = []
        if root == None:
            return ret
        if root.left != None:
            ret += inorderTraversal(root.left)
        ret.append(root)
        if root.right != None:
            ret += inorderTraversal(root.right)
        return ret

    nodes = inorderTraversal(root)
    num = nodes.__len__() - 1
    exchange = True
    while num != 0 and exchange:
        exchange = False
        for i in range(0, num):
            if nodes[i].val > nodes[i + 1].val:
                nodes[i].val = nodes[i].val ^ nodes[i + 1].val
                nodes[i + 1].val = nodes[i].val ^ nodes[i + 1].val
                nodes[i].val = nodes[i].val ^ nodes[i + 1].val
                exchange = True
        num -= 1

def showTree(root, len=1):
    BLANK = ' '
    NONENODE = '.'
    len = len + (len + 1) % 2
    lines_levels = []
    nodes_levels = []
    nodes = []
    if root == None:
        return
    else:
        nodes.append(root)
        nodes_levels.append(nodes)
    while nodes.__len__():
        count = 0
        temp_nodes = []
        for node in nodes:
            if node == None:
                temp_nodes.append(None)
                temp_nodes.append(None)
                count += 1
            else:
                temp_nodes.append(node.left)
                temp_nodes.append(node.right)
                if node.left == None and node.right == None:
                    count += 1
        if count == nodes.__len__():
            break
        else:
            nodes_levels.append(temp_nodes)
        nodes = temp_nodes
    level = nodes_levels.__len__()
    i = 0
    for ns in nodes_levels:
        first = 2 ** (level - i)
        first = first * len
        second = 2 ** (level - i - 1)
        second = second * len
        line = BLANK * (second - len)
        index = 0
        for n in ns:
            if n:
                    line += ('{0:^' + '{}'.format(len) + 'd}' + '{1}').format(n.val, BLANK * (first - len))
            else:
                    line += (BLANK * (len // 2)) + NONENODE + (BLANK * (len // 2)) + BLANK * (first - len)
            index += 1
        lines_levels.append(line)
        i += 1

    for l in lines_levels:
        print(l)