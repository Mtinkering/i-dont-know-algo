# Enter your code here. Read input from STDIN. Print output to STDOUT
T = input()

def bfs(s,graph,U):
	next_node = [s]
	level = {s:0}
	i = 1

	while len(next_node) > 0:
		nextTovisit = []
		for u in next_node:
			if (u not in graph): continue
			for v in graph[u]:
				if v not in level:
					level[v] = i
					nextTovisit.append(v)
		i +=  1
		next_node = nextTovisit

	for j in range(1,U+1):
		if (j == s): continue
		if (j in level):
			print level[j]*6,
		else:
			print -1,
	print

for _ in range(T):
	U, M = [int(x) for x in raw_input().split()]
	graph = {}
	for i in range(M):
		a, b = [int(x) for x in raw_input().split()]
		if a not in graph:
			graph[a] = []
		if b not in graph[a]:
			graph[a].append(b)

		#Remove this if you want a Directed Graph
		if b not in graph:
			graph[b] = []
		if a not in graph[b]:
			graph[b].append(a)

	s = input()
	# print graph
	bfs(s,graph,U)




