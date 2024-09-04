arr = [5, 3, 2, 5, 7, 1, 4, 6, 4, 3, 8, 2]
x = 5

sliding_window = sum(arr[:x]) # 처음 x개의 합 구하기, 0번부터 x-1번까지
print('sliding window start', sliding_window)

# x-1번 인덱스의 값들의 합을 구했으므로 반복문은 x번 인덱스부터 시작.
for i in range(x, len(arr)):
	sliding_window -= arr[i - x]
	sliding_window += arr[i]
	print(sliding_window)


