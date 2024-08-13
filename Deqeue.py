class DoubleNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None:
            return "Empty!"
        res = ""
        node = self.head
        while node.next is not None:
            res += str(node.data) + " ↔ "
            node = node.next
        return res + str(node.data)

    def __contains__(self, data):
        if self.head is None:
            return False

        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next

        return False

    def appendleft(self, data):
        new_node = DoubleNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def append(self, data):
        new_node = DoubleNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def popleft(self):
        if self.head is None:
            return

        node = self.head
        if self.head == self.tail:
            self.head.next = self.tail.prev = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return node.data

    def pop(self):
        if self.tail is None:
            return

        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return node.data

    def insert(self, i, data):
        if i <= 0:
            self.popleft(data)
        elif i >= len(self):
            self.pop(data)
        else:
            new_node = DoubleNode(data)
            current_node = self.head

            for _ in range(i):
                current_node = current_node.next

            new_node.next = current_node
            new_node.prev = current_node.prev
            current_node.prev.next = new_node
            current_node.prev = new_node
        self.length += 1

    def remove(self, data):
        if self.head is None:
            return

        current_node = self.head
        while current_node:
            if current_node.data == data:
                break
            current_node = current_node.next

        if current_node is None:
            return

        if current_node.prev:
            current_node.prev.next = current_node.next

        if current_node.next:
            current_node.next.prev = current_node.prev

        if self.head == current_node:
            self.head = current_node.next

        if self.tail == current_node:
            self.tail = current_node.prev

        self.length -= 1
        return True

    def reverse(self):
        prev, current = None, self.head
        while current:
            next, current.next = current.next, prev
            current.prev = next
            prev, current = current, next
        self.head, self.tail = self.tail, self.head

deq = Deque()
for i in range(5):
    deq.append(i)

print(f"원래 상태: {deq},  head = {deq.head.data},  tail = {deq.tail.data}")
print()
deq.reverse()
print(f"뒤집은 상태: {deq},  head = {deq.head.data},  tail = {deq.tail.data}")