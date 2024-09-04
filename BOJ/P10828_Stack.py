import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.last = None
        self.length = 0

    def size(self):
        print(self.length)

    def push(self, data):
        self.last = Node(data, self.last)
        self.length += 1

    def empty(self):
        print(1 if self.length <= 0 else 0)

    def pop(self):
        if self.last is None:
            print(-1)
            return

        result = self.last.data
        self.last = self.last.next
        self.length -= 1

        print(result)

    def top(self):
        if self.last is None:
            print(-1)
            return
        print(self.last.data)

    def do(self, instruction):
        print(instruction[0])
        if instruction[0] == 'push':
            self.push(instruction[1])
        elif instruction[0] == 'top':
            self.top()
        elif instruction[0] == 'size':
            self.size()
        elif instruction[0] == 'pop':
            self.pop()
        elif instruction[0] == 'empty':
            self.empty()


my_stack = Stack()
for _ in range(int(input().rstrip())):
    my_stack.do(input().rstrip().split())