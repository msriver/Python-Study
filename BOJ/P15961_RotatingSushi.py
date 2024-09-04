import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().rstrip().split())
arr = [int(input().rstrip()) for _ in range(n)]

sushi = [0] * (d + 1)
sushi[c] = 1
eat_sushi = 1

# print('------------초기 검사 start-----------')
for i in arr[:k]:
    # print('현재 검사중인 스시', i)
    # print('지금까지 이 스시는', sushi[i], '개 먹었음')
    sushi[i] += 1
    if sushi[i] == 1:
        eat_sushi += 1

# print('초기 eat_sushi', eat_sushi)
# print('------------초기 검사 end-----------')

max_count = eat_sushi

for i in range(1, n):
    prev_index = i - 1 # 빼줘야할 인덱스
    next_index = (i + k - 1) % n # 더해줘야할 인덱스

    sushi[arr[prev_index]] -= 1
    if sushi[arr[prev_index]] == 0:
        eat_sushi -= 1

    sushi[arr[next_index]] += 1
    if sushi[arr[next_index]] == 1:
        eat_sushi += 1

    max_count = max(eat_sushi, max_count)

print(max_count)