import collections

arr = ['A', 'B', 'C', 'D', 'E', 'F', None, 'G']

# 전위 순회 함수, 현 - 왼 - 오
def preorder_traversal(tree):
    def _preorder_traversal(index):
        if index >= len(tree) or tree[index] is None:
            return None

        res.append(tree[index])
        _preorder_traversal(2 * index + 1)
        _preorder_traversal(2 * index + 2)

    res = []
    _preorder_traversal(0)
    return res

# 중위 순회, inorder, 왼 - 부 - 오
def inorder_traversal(tree):
    def _inorder_traversal(index):
        if index >= len(tree) or tree[index] is None:
            return

        _inorder_traversal(2 * index + 1)
        res.append(tree[index])
        _inorder_traversal(2 * index + 2)

    res = []
    _inorder_traversal(0)
    return res

# 후위 순회, postorder, 왼 - 오 - 부
def postorder_traversal(tree):
    def _postorder_traversal(index):
        if index >= len(tree) or tree[index] is None:
            return

        _postorder_traversal(2 * index + 1)
        _postorder_traversal(2 * index + 2)
        res.append(tree[index])

    res = []
    _postorder_traversal(0)
    return res

# 전위 순회, 스택을 이용한 방법, 부 왼 오
def preorder(arr):
    if arr is None or len(arr) == 0:
        return

    res = []
    stack = [0] # 방문해야할 인덱스 저장

    while stack:
        parent_index = stack.pop()
        res.append(arr[parent_index]) # 부모 먼저

        left_child_index = 2 * parent_index + 1
        right_child_index = left_child_index + 1

        # 스택에 오른쪽을 먼저 넣어야, 왼쪽이 먼저 나오게 된다.
        # 왼쪽을 먼저 돌아야하기 때문에 순서를 이렇게 해서 스택에 넣어준다.
        if right_child_index < len(arr) and arr[right_child_index] is not None:
            stack.append(right_child_index)

        if left_child_index < len(arr) and arr[left_child_index] is not None:
            stack.append(left_child_index)

    return res

# 중위 순회, 왼 부 오
def inorder(arr):
    if not arr:
        return

    res = []
    stack = []

    index = 0
    while True:
        if index < len(arr) and arr[index]:
            stack.append(index)
            index = 2 * index + 1
        elif stack:
            index = stack.pop()
            res.append(arr[index])
            index = 2 * index + 2
        else:
            break

    return res

# 후위 순회, 왼 오 부
def postorder(arr):
    if not arr:
        return

    res = []
    stack = [0]
    visit_order = []

    while stack:
        parent = stack.pop()
        visit_order.append(parent)

        left_child = 2 * parent + 1

# 레벨 순서 순회
# 위 세 순회들과는 다르게 스택이 아니라 큐를 사용하여 풀이.
def levelorder(arr):
    if not arr:
        return

    res = []
    deq = collections.deque()
    deq.append(0)

    index = 0
    while deq:
        index = deq.popleft()
        res.append(arr[index])

        child_index = 2 * index + 1
        if child_index < len(arr) and arr[child_index]:
            deq.append(child_index)

        child_index += 1
        if child_index < len(arr) and arr[child_index]:
            deq.append(child_index)

    return res