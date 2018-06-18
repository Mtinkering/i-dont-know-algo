


for _ in range(0,input()):
	M,N = [int(x) for x in raw_input().split()]
	CY = sorted([int(x) for x in raw_input().split()], reverse=True)
	CX = sorted([int(x) for x in raw_input().split()], reverse=True)
	nx = 1
	ny = 1
	minC = 0
	i = 0
	j = 0
	total = M - 1 + N - 1
	for _ in range(0,total):
		if (j == N - 1 or (i != M -1 and CY[i] > CX[j])):
			minC += CY[i]*nx
			ny += 1
			i += 1
		else:
			minC += CX[j]*ny
			nx += 1
			j += 1

	print minC%(1000000000+7)
