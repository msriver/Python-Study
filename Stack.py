class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            return

        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            return None

        current = self.top
        self.top = current.next

        return current.data

    def peek(self):
        if self.top is None:
            return None

        return self.top.data

    def is_empty(self):
        return self.top is None