import bisect
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = [int(x) for x in input().rstrip().split()]
arr.sort()

m = int(input().rstrip())
targets = [int(x) for x in input().rstrip().split()]

for target in targets:
    idx = bisect.bisect_left(arr, target)
    if idx < len(arr) and arr[idx] == target:
        print(1)
    else:
        print(0)
