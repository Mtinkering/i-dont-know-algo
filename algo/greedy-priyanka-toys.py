N = int(raw_input())

W = sorted(map(int, raw_input().split()))

current_max = W[0] + 4
answer = 1
if N != 1:
	for i in range(1,N):
		if W[i] > current_max:
			current_max = W[i] + 4
			answer += 1

print answer
