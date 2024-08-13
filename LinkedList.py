
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if self.head is None:
            return 'No Data'
        result = ['Head']
        current_node = self.head
        while current_node:
            result.append(str(current_node.data))
            current_node = current_node.next

        return " -> ".join(result)

    # 연결 리스트 맨 끝에 값 추가하기
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.length += 1
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = Node(data)
        self.length += 1

    # 연결 리스트 맨 앞에 값 추가하기
    def appendleft(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    # 연결 리스트 맨 끝의 값 추출하기
    def pop(self):
        if self.head is None:
            return None

        parent_node = None
        current_node = self.head
        while current_node.next:
            parent_node = current_node
            current_node = current_node.next

        if current_node == self.head:
            self.head = None
        else:
            parent_node.next = None
        self.length -= 1
        return current_node.data

    def popleft(self):
        if self.head is None:
            return None

        node = self.head

        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
        self.length -= 1
        return node.data

    def remove(self, data):
        if self.head is None:
            return None

        parent_node = None
        current_node = self.head

        while current_node:
            if current_node.data == data:
                break
            parent_node = current_node
            current_node = current_node.next

        if not current_node:
            return None
        else:
            if current_node == self.head:
                self.head = current_node.next
            else:
                parent_node.next = current_node.next

            self.length -= 1

    def insert(self, i, data):
        if self.head is None:
            self.head = Node(data)
            self.length += 1
        elif i == 0:
            self.appendleft(data)
        elif i == self.length - 1:
            self.append(data)
        else:
            index = 0
            parent = None
            current_node = self.head
            while current_node:
                if index == i:
                    break
                index += 1
                parent = current_node
                current_node = current_node.next

            new_node = Node(data)
            new_node.next = current_node
            parent.next = new_node
            self.length += 1

    def reverse(self):
        if self.head is None or self.length <= 1:
            return None

        prev = None
        ahead = self.head.next

        while ahead:
            self.head.next = prev
            prev = self.head
            self.head = ahead
            ahead = ahead.next

        # 요 부분이 중요함.
        # 이걸 안하면 연결 정보들을 다 잃어버려.
        # next가 존재하는 동안 루프가 돌잖아.
        # 그럼 next가 존재하지 않는 시점에
        # self.head(current)와 prev를 한번 이어줘야 하는데
        # while문이 안도니깐 저게 안돈단말이야
        # 그래서 while문 밖에서 한번 더 이어줘야함.
        self.head.next = prev



ll = LinkedList()
ll.append(4)
ll.append(2)
ll.append(3)
print(ll)
print(len(ll))

ll.insert(0, 9)
print(ll)
print(len(ll))

ll.insert(2, 8)
print(ll)

ll.reverse()
print(ll)