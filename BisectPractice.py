
def binary_search(arr, x):
    arr.sort()

    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1

    return -1