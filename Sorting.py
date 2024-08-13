import sys
sys.setrecursionlimit(10 ** 6)


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_val = float('inf')
        min_val_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min_val:
                min_val = arr[j]
                min_val_index = j

        arr[min_val_index] = arr[i]
        arr[i] = min_val

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
                i = j

def merge_sort(arr):
    def _merge(left_divided_arr, right_divided_arr):
        res = []
        left = right = 0
        while left_divided_arr or right_divided_arr:

            if left >= len(left_divided_arr):
                while right < len(right_divided_arr):
                    res.append(right_divided_arr[right])
                    right += 1
                break

            elif right >= len(right_divided_arr):
                while left < len(left_divided_arr):
                    res.append(left_divided_arr[left])
                    left += 1
                break

            if left_divided_arr[left] <= right_divided_arr[right]:
                min_val = left_divided_arr[left]
                left += 1
            else:
                min_val = right_divided_arr[right]
                right += 1

            res.append(min_val)
        return res

    def _divide(current_arr):
        if len(current_arr) == 1:
            return current_arr
        mid_index = (len(current_arr)) // 2
        left_divided_arr = _divide(current_arr[0:mid_index])
        right_divided_arr = _divide(current_arr[mid_index:])
        return _merge(left_divided_arr, right_divided_arr)

    return _divide(arr)

import random
my_list = []
for _ in range(10):
    my_list.append(random.randrange(15))

print("정렬 전:")
print(my_list)
print()
print("정렬 후:")
result = merge_sort(my_list)
print(result)