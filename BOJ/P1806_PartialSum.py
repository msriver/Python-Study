import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split())
arr = [int(x) for x in input().rstrip().split()]

left = right = 0
sum = 0
min_size = len(arr) + 1

while right < len(arr):
    sum += arr[right]

    while sum >= s and left <= right:
        min_size = min(min_size, (right - left + 1))
        sum -= arr[left]
        left += 1

    right += 1

print(min_size if min_size <= len(arr) else 0)

