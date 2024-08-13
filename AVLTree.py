from BinarySearchTree import Node, BSTree

class AVLNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.height = 0

class AVLTree(BSTree):

    def get_height(self, node):
        if node is None:
            return -1

        left_height = node.left.height if node.left else -1
        right_height = node.right.height if node.right else -1

        return 1 + max(left_height, right_height)

    def get_bf(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def _insert(self, node, data):
        if node is None:
            return AVLNode(data)

        if node.data > data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        node.height = self.get_height(node)
        node = self.balencing(node)
        return node

    def right_rotate(self, node):
        child = node.left

        child.right, node.left = node, child.right

        node.height = self.get_height(node)
        child.height = self.get_height(child)

        return child

    def left_rotate(self, node):
        child = node.right

        child.left, node.right = node, child.left

        node.height = self.get_height(node)
        child.height = self.get_height(child)

        return child

    def left_right_rotate(self, node):
        child = node.left
        grandchild = child.right

        child.right, node.left = grandchild.left, grandchild.right
        grandchild.left, grandchild.right = child, node

        child.height = self.get_height(child)
        node.height = self.get_height(node)
        grandchild.height = self.get_height(grandchild)

        return grandchild

    def right_left_rotate(self, node):
        child, grandchild = node.right, node.right.left

        node.right, child.left = grandchild.left, grandchild.right
        grandchild.left, grandchild.right = node, child

        child.height = self.get_height(child)
        node.height = self.get_height(node)
        grandchild.height = self.get_height(grandchild)

        return grandchild

    def balencing(self, node):
        bf = self.get_bf(node)
        if bf >= 2:
            if self.get_bf(node.left) >= 0:
                node = self.right_rotate(node)
            else:
                node = self.left_right_rotate(node)
        elif bf <= -2:
            if self.get_bf(node.right) >= 0:
                node = self.left_rotate(node)
            else:
                node = self.right_left_rotate(node)

        return node

#트리를 받아서 레벨 순서 순회하며 값을 출력하는 함수
def level_order(tree):
    q = [tree.root]
    res = []

    while q:
        node = q.pop(0)
        res.append((node.data, node.height, tree.get_bf(node)))
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return res


tree = AVLTree()
for x in (8, 3, 10, 1, 6, 9, 12, 4, 5, 11):
    tree.insert(x)
    print(level_order(tree))