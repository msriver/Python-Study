class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        node = Node(data)

        if self.front is None:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            return None

        node = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return node.data

    # 스택을 이용하여 뒤집을 수 있다.
    # 큐가 빌때까지 스택에 집어넣는다.
    # 스택이 빌때까지 큐에 enqueue한다.
    def reverse(self):
        stack = []
        while self.front:
            stack.append(self.dequeue())

        while stack:
            self.enqueue(stack.pop())


