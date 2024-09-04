import sys
input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
arr = [int(x) for x in input().rstrip().split()]

window = max_sum = sum(arr[:x])
max_cnt = 1

