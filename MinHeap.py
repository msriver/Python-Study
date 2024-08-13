"""
파이썬 내장 자료형인 heapq를 직접 구현해본다.
최소 힙을 만족하도록 구현한다.
구현 메서드는 다음과 같다.
    1. heappush: 힙에 데이터를 삽입한다.
    2. heappop: 힙의 루트 노드값을 꺼낸 후 삭제한다.
    3. heapify: 배열을 입력받아 힙 구조로 만든다.
"""

# 기본적으로 배열을 가지고 다룬다.
class Heap:

    # 힙 끝단에 새로운 값을 먼저 집어 넣는다.
    # 새로운 노드의 값이 부모보다 작으면 부모와 위치를 바꾼다.
    @staticmethod
    def heappush(heap_arr, data):
        if not heap_arr:
            return

        heap_arr.append(data)
        new_data_index = len(heap_arr) - 1
        while True:
            parent_index = (new_data_index - 1) // 2

            if parent_index < 0 or heap_arr[parent_index] <= heap_arr[new_data_index]:
                break
            else:
                heap_arr[parent_index], heap_arr[new_data_index] = heap_arr[new_data_index], heap_arr[parent_index]
                new_data_index = parent_index

    # 힙에서 루트 노드를 꺼낸다.
    # 힙 배열의 마지막 값을 루트로 대체한다. 마지막값은 pop()으로 빼내와서 옮기는 것이다.
    @staticmethod
    def heappop(arr):
        if not arr:
            return None
        elif len(arr) <= 2:
            return arr.popleft()
        else:
            result = arr[0]
            arr[0] = arr.pop()

            index = 0
            child_index = 1

            while child_index < len(arr):
                sibling_index = child_index + 1

                # 형제 중에 더 작은놈을 고른다.
                # 형제 중 더 큰놈은 다른 형제를 제끼고 위로 못올라가기 때문이다. (최소힙 특성상)
                if sibling_index < len(arr) and arr[sibling_index] < arr[child_index]:
                    child_index = sibling_index

                if arr[child_index] < arr[index]:
                    arr[index], arr[child_index] = arr[child_index], arr[index]
                    index = child_index
                    child_index = 2 * child_index + 1
                else:
                    break

            return result

    @staticmethod
    def heapify(arr):
        last_parent_index = len(arr) // 2 - 1

        for current in range(last_parent_index, -1, -1):

            while current <= last_parent_index:
                child = current * 2 + 1
                slbling = child + 1

                if slbling < len(arr) and child < len(arr) and arr[slbling] < arr[child]:
                    child = slbling

                if child < len(arr) and arr[child] < arr[current]:
                    arr[current], arr[child] = arr[child], arr[current]
                    current = child
                else:
                    break