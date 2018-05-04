class TreeNode:
    def __init__(self, key, value, left_child=None,
                 right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def replace(self, key, value, left_child,
                right_child, parent):
        self.key = key
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def has_left_child(self):
        return self.left_child

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def has_right_child(self):
        return self.right_child

    def has_any_child(self):
        return not self.is_leaf()

    def has_both_child(self):
        return self.left_child and self.right_child

    def is_root(self):
        return self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        else:
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
            elif self.has_right_child():
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def __iter__(self):
        if self:
            if self.has_left_child():
                for item in self.left_child:
                    yield item
            yield self.key
            if self.has_right_child():
                for item in self.right_child:
                    yield  item

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0
    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size += 1

    def _put(self, key, value, node):
        if key < node.key:
            if node.has_left_child():
                self._put(key, value, node.left_child)
            else:
                node.left_child = TreeNode(key, value)
        else:
            if node.has_right_child():
                self._put(key, value, node.right_child)
            else:
                node.right_child = TreeNode(key, value)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            ret = self._get(key, self.root)
            if ret:
                return ret
            else:
                return None
        else:
            return None

    def _get(self, key, node):
        if not node:
            return None
        elif node.key == key:
            return node
        elif node.key < key:
            self._get(key, node.right_child)
        elif node.key > key:
            self._get(key, node.left_child)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self.get(item):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            node = self.get(key)
            if node:
                self.remove(node)
            else:
                raise KeyError('no {} key'.format(key))
        elif self.root and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('empty tree, no {} key'.format(key))

    def remove(self, current_node):
        #leaf
        if current_node.is_leaf():
            if current_node.parent.left_child == current_node:
                current_node.parent.left_child = None
            elif current_node.parent.right_child == current_node:
                current_node.parent.right_child = None
        elif current_node.has_both_child():
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.value = succ.value

        else:
            if current_node.has_left_child:
                if current_node.is_left_child:
                    current_node.parent.left_child = current_node.left_child
                    current_node.left_child.parent = current_node.parent
                elif current_node.is_right_child:
                    current_node.parent.right_child = current_node.left_child
                    current_node.left_child.parent = current_node.parent
                else:
                    current_node.replace(current_node.left_child.key, current_node.left_child.value,
                                        current_node.left_child.left_child, current_node.left_child.right_child,
                                        current_node.parent)
            else:
                if current_node.is_left_child:
                    current_node.parent.left_child = current_node.right_child
                    current_node.right_child.parent = current_node.parent
                elif current_node.is_right_child:
                    current_node.parent.right_child = current_node.right_child
                    current_node.right_child.parent = current_node.parent
                else:
                    current_node.replace(current_node.right_node.key, current_node.right_node.value,
                                         current_node.right_child.left_child, current_node.right_child.right_child,
                                         current_node.parent)

    # def __del__(self, item):
    #     self.delete(item)

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

if __name__ == '__main__':
    btree = BinarySearchTree()
    btree[1] = 'red'
    btree[6] = 'grey'
    btree[4] = 'green'
    btree[7] = 'pink'
    btree[2] = 'orange'
    btree[3] = 'yellow'
    btree[5] = 'blue'

    # #__iter__
    # for i in btree:
    #     print(i)
    #
    # #__contains__
    # print(1 in btree)
    # print(8 in btree)
    #
    # #delete
    # btree.delete(6)
    #
    # for i in btree:
    #     print(i)

    print(btree[1])
    print(btree[2])