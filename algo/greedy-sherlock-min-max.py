N = int(raw_input())

A = [int(x) for x in raw_input().split()]

P, Q = [int(x) for x in raw_input().split()]

currentMin = -1
currentM = -1
for i in range(P,Q+1):
	minDiff = 2*1000000000
	for j in range(0,N):
		diff = A[j] - i
		if (diff < 0):
			diff = -diff
		minDiff = min(minDiff, diff)

	if (minDiff > currentMin):
		currentMin = minDiff
		currentM = i

print currentM