from collections import deque

n, k = map(int, input().split())

deq = deque()
for i in range(1, n + 1):
    deq.append(str(i))
res = []

idx = 1
while deq:
    person = deq.popleft()

    if idx % k == 0:
        res.append(person)
    else:
        deq.append(person)
    idx += 1

print(f'<{", ".join(res)}>')