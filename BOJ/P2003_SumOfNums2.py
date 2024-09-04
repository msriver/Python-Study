import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
arr = [int(x) for x in input().rstrip().split()]

left = right = 0
sum = 0
ans = 0

while right < len(arr):
    sum += arr[right]

    while sum > m and left < right:
        sum -= arr[left]
        left += 1

    if sum == m:
        ans += 1

    right += 1

print(ans)