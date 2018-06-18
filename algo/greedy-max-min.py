N = input()
K = input()
lists = [input() for _ in range(0,N)]
lists.sort()

min_diff = 2000000000
diff = 0
for i in range(0,N-K+1):
	diff = lists[i+K-1] - lists[i]
	min_diff = min(min_diff,diff)


print min_diff