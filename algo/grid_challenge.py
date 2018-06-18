T = int(raw_input())
for test in range(T):
	N = int(raw_input())
	G = []
	for n in range(N):
		line = raw_input()
		G.append(sorted(list(line)))

	G.append(G[-1])

	answer = 'YES'
	i = 0
	while i < N:

		for j in range(N):
			if (G[i][j] > G[i+1][j]):
				answer = 'NO'
				break
				i = N + 1
		
		i += 1

	print answer

