T = int(raw_input())

for _ in range(T):
	M = int(raw_input())
	N = int(raw_input())
	arr = [int(x) for x in raw_input().split()]
	def _helper():

		for i in range(N):
			for j in range(i+1,N):
				if (arr[i] + arr[j] == M):
					print i+1, j+1
					return
	_helper()
