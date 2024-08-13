import collections

# 문제 1
# 정수 배열에서 가장 큰 두 수를 찾아라
# 정수로 이루어진 배열이 주어질 때, 가장 큰 두 수를 찾아 가장 큰값, 두번째로 큰 값을 배열로 반환하라.
def solution1_1(arr):
    return sorted(arr)[:-3:-1]

def solution1_2(arr):
    max_1, max_2 = arr[0], arr[1]
    if max_2 > max_1:
        max_1, max_2 = max_2, max_1

    for num in arr[2:]:
        if num > max_1:
            max_1, max_2 = num, max_1
        elif num > max_2:
            max_2 = num

    return [max_1, max_2]

# 문제 1 테스트
input_arr = [1, 9, 3, 10, 5, 11, 2, 13]

res1 = solution1_1(input_arr)
print('solution1_1', res1)

res2 = solution1_2(input_arr)
print('solution1_2', res2)


# 문제 2
# 어떤 문자열이 주어졌을 때, 팰린드롬이면 True, 아니면 False를 출력하라.
def solution2_1(string):
    return string == string[::-1]

def solution2_2(string):
    start, end = 0, len(string) - 1
    while start < end:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

def solution2_3(string):
    deq = collections.deque()
    for c in string:
        deq.append(c)

    while deq:
        if deq.pop() != deq.popleft():
            return False
    return True

# 문제 2 테스트
input_string_2_1 = 'tomato'
input_string_2_2 = 'mazzam'

print('solution2_1', solution2_1(input_string_2_1))
print('solution2_1', solution2_1(input_string_2_2))

print('solution2_2', solution2_2(input_string_2_1))
print('solution2_2', solution2_2(input_string_2_2))

print('solution2_3', solution2_3(input_string_2_1))
print('solution2_3', solution2_3(input_string_2_2))


# 문제 3
# 0과 1로 구성된 배열 정렬하기
# 0과 1로 이루어진 배열을 오름차순으로 정렬하라.
def solution3_1(arr):
    return sorted(arr)

def solution3_2(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        while start < len(arr) and arr[start] == 0:
            start += 1

        while end > start and arr[end] == 1:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start, end = start + 1, end - 1

    return arr

input_arr_3 = [0, 1, 0, 1, 0, 0, 0, 1, 1, 0]
input_arr_3_1 = [0, 0, 0, 0, 1, 1, 1, 1]
print('solution3_1', solution3_1(input_arr_3))
print('solution3_2', solution3_2(input_arr_3))


# 문제 4
# 제시된 합을 찾는 부분 배열 찾기
# 정렬되지 않은 양의 정수 배열이 주어진다. 연속된 원소를 더한 값이 제시된 값 S와 일치하는 부분 배열을 찾아라.
# 시간복잡도 O(N)에 풀이하라.
def solution4_1(arr, s):
