T  = int(raw_input())

for _ in range(T):
	N,K = map(int, raw_input().split())
	A = sorted(map(int, raw_input().split()))
	B = sorted(map(int, raw_input().split()), reverse=True)
	answer = 'YES'
	for i in range(N):
		if A[i] + B[i] < K:
			answer = 'NO'
			break
	print answer