class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def show_tree(root):
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
                count += 1
                temp_nodes.append(None)
                temp_nodes.append(None)
            else:
                temp_nodes.append(node.left)
                temp_nodes.append(node.right)
        if count == nodes.__len__():
            break
        else:
            nodes_levels.append(temp_nodes)
        nodes = temp_nodes
    level = nodes_levels.__len__()
    i = 0
    for ns in nodes_levels:
        temp_levels = []
        first = 2 ** (level - i)
        second = 2 ** (level - i - 1)
        for l in lines_levels:
            temp_l = (' ' * (second)) + l
            temp_levels.append(temp_l)
        lines_levels = temp_levels
        line = ''
        index = 0
        for n in ns:
            if n:
                if index % 2 == 0:
                    line += '{0}{1}'.format(n.val, ' ' * (first - 1))
                else:
                    line += '{0}{1}'.format(n.val, ' ' * (first - 1))
            else:
                if index % 2 == 0:
                    line += '.' + ' ' * (first - 1)
                else:
                    line += '.' + ' ' * (first - 1)
            index += 1
        lines_levels.append(line)
        i += 1

    for l in lines_levels:
        print(l)