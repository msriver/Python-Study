import sys
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(k)]

max_line = max(arr)

start = 1 # 이게 왜 1이 되어야 하는지 잘 생각해보자.
end = max_line
ans = 0

while start <= end:
    mid = (start + end) // 2

    temp_count = 0
    for line in arr:
        temp_count += line // mid

    if temp_count >= n:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
