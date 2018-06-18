# N = input()
# V = {}
# for i in raw_input().split():
# 	if i in V:
# 		V[i] += 1
# 	else:
# 		V[i] = 1

# maxI = -1
# for i in V:
# 	maxI = max(maxI, V[i])


# print N - maxI

N, K = [int(x) for x in raw_input().split()]

N_TOWERS = [int(n) for n in raw_input().split()]

answer = -1
minX = 0
R = K - 1
counter = 0
flag = True
while flag and (minX < N):
	minX_Try = minX + R
	flag = False
	if (minX_Try >= N): minX_Try = N - 1
	if (N_TOWERS[minX_Try] == 1):
		minX = minX_Try + R + 1
		counter += 1
		flag = True
	else:
		for X in range(minX_Try - 1, minX - 1 - R, -1):
			if (N_TOWERS[X] == 1):
				minX = X + R + 1
				counter += 1
				flag = True
				break
	answer = counter
	if (not flag):
		answer = -1
print answer





