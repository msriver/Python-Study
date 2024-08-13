class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def inorder_print(self):
        def _inorder(node):
            if node is None:
                return

            _inorder(node.left)
            res.append(node.data)
            _inorder(node.right)

        res = []
        _inorder(self.root)
        return res

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if node.data > data:
            node.left = self._insert(node.left)
        elif node.data < data:
            node.right = self._insert(node.right)

        return Node(data)
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def delete(self, data):
        def _delete(node):
            if node is None:
                return

            if node.data > data:
                node.left = _delete(node.left)
            elif node.data < data:
                node.right = _delete(node.right)
            else:
                if node.left is None or node.right is None:
                    if node.left is None:
                        child = node.right
                    else:
                        child = node.left

                    return child

                else:
                    successor = node.right
                    successor_parent = node
                    while successor.left:
                        successor_parent = successor
                        successor = successor.left

                    node.data = successor.data
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    elif successor_parent.right == successor:
                        successor_parent.right = successor.right

            return node

        self.root = _delete(self.root)
