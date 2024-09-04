
def is_valid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif stack and stack[-1] == '(':
            stack.pop()
        else:
            return 'NO'

    return 'NO' if stack else 'YES'

for _ in range(int(input())):
    is_valid(input())