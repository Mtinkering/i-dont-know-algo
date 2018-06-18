vertices, edges = [int(x) for x in raw_input().split()]

for i in range(0,edges):
	

graph = {}

def BFS(s, Adj):
	#visit all the nodes reachable from given S in V
	#O(V+E) time
	#look at all the nodes reachable in zero move,1 move, 2 moves until we run out of graph
	#avoid duplicates

	level = {s:0}
	parent = {s: None}
	i = 1
	frontier = [s]

	while frontier:
		nextToVist = []
		for u in frontier:
			for v in Adj[u]:
				if v not in level:
					level[v] = i
					parent[v] = u
					nextToVist.append(v)
		frontier = nextToVist
		i += 1







