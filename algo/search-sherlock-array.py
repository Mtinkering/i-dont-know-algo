T = int(raw_input())

for _ in range(T):
	N = int(raw_input())
	arr = [int(x) for x in raw_input().split()]
	left = 0
	right = sum(arr[1:])

	if N == 1:
		print 'YES'
	else:
		result = 'NO'
		for i in range(1,N):
			left += arr[i-1]
			right -= arr[i]
			if (left == right):
				result = 'YES'
				break

		print result

