import sys
input = sys.stdin.readline

# 1. 파이썬의 heapq 모듈을 이용하여 풀이하기
import heapq

arr = []

for _ in range(int(input().rstrip())):
    x = int(input().rstrip())
    if x:
        heapq.heappush(arr, -x)
    else:
        if len(arr) > 0:
            res = heapq.heappop(arr)
            print(-res)
        else:
            print(0)



####################################################################
####################################################################
####################################################################

# 2. 직접 Heap 클래스 구현해보기
# 직접 제출을 해보니 1번보다 속도 자체는 느렸다. 그러나 정상 통과하긴 하였다.

class Heap:

    # left child = 2 * index + 1
    # right child = 2 * index + 2
    # parent index = (child index - 1)  // 2
    @staticmethod
    def heappush(arr, x):
        arr.append(x)
        current_index = len(arr) - 1
        while current_index >= 0 and current_index < len(arr):
            parent_index = (current_index - 1) // 2
            if parent_index >= 0 and arr[parent_index] < arr[current_index]:
                arr[parent_index], arr[current_index] = arr[current_index], arr[parent_index]
                current_index = parent_index
            else:
                break

    @staticmethod
    def heappop(arr):
        if not arr:
            print(0)
            return
        elif len(arr) == 1:
            print(arr.pop())
            return

        root = arr[0]
        arr[0] = arr.pop()
        current = 0

        while current < len(arr):
            child = 2 * current + 1
            sibling = child + 1
            if sibling < len(arr) and arr[sibling] > arr[child]:
                child = sibling

            if child < len(arr) and arr[current] < arr[child]:
                arr[current], arr[child] = arr[child], arr[current]
                current = child
            else:
                break

        print(root)

arr = []
for _ in range(int(input().rstrip())):
    x = int(input().rstrip())
    if x:
        Heap.heappush(arr, x)
    else:
        Heap.heappop(arr)
