# https://www.acmicpc.net/problem/2750
# n = int(input())
#
# arr = []
# for _ in range(n):
#     arr.append(int(input()))

# 선택 정렬
# 1. 전체에서 가장 작은 수를 맨 앞으로 보냄.
# 2. 두번째부터 끝까지 탐색하여 가장 작은 수를 두번째로 보냄
# 3. 세번째부터 끝까지 탐색하여 가장 작은 수를 세번째로 보냄
# 4. 쭉쭉 가다가, 마지막에서 두번째 수부터 마지막까지 탐색하여 가장 작은 수를 마지막에서 두번째로 보냄. 마지막은 자동으로 제일 큰 수가 됨.
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 버블 정렬
# 현재 요소와 바로 그 다음 요소를 비교하여 큰 수를 뒤으로 보냄. 끝까지 반복하면 제일 큰 수가 뒤에 있게 됨
# 다시 제일 뒤에서 두번째까지 반복
# 다시 제일 뒤에서 세번째까지 반복... 쭉쭉
# 4 3 2 1
# 3 4 2 1
# 3 2 4 1
# 3 2 1 4
# 2 3 1 4
# 2 1 3 4
# 1 2 3 4
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

# 삽입 정렬
# 정렬되지 않은 리스트에서 현재 인덱스의 값을 그 왼쪽의 부분배열의 모든 요소들과 비교하여
# 자리를 찾아주는 정렬방법
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i - 1, -1, -1): # i의 바로 왼쪽부터 배열의 끝 0번인덱스까지 거꾸로 탐색.
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = j

arr = [3, 2, 1, 5, 4]
insertion_sort(arr)
print(*arr)

