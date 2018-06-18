
N, M = [int(x) for x in raw_input().split()]
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

# Method 1: but not efficient because we have to transvere multiple times
# but avoid recursion
# hmm, possible using DP ?
# cant avoid recursion, because this is depth first search = explore the graph in depth first

def breakTheEdge(Adj,v,e):
	Adj[v].remove(e)
	Adj[e].remove(v)


def NumberOfChildren(Adj, s, root):

	parent = {s:None, root: None}  #ignore the root way
	def DFSVisit(Adj, s):
		for v in Adj[s]:
			if v not in parent:
				parent[v] = s
				DFSVisit(Adj, v)
	DFSVisit(Adj, s)
	return len(parent) - 1

visited = {}
answer = 0

def dfs(Adj, s):
	global answer
	visited[s] = True
	num_vertex = 0
	for v in Adj[s]:
		if v not in visited:
			num_nodes = dfs(Adj, v)
			if (num_nodes % 2 == 0):
				answer += 1
			else:
				num_vertex += 1

	return num_vertex+1




#method 2
dfs(graph, 1)

# for root in graph:
# 	length = len(graph[root])
# 	if (length > 1):
# 		children  = graph[root][:]
# 		for child in children:
			# n = NumberOfChildren(graph, child, root)
			# if (n and n % 2 == 0):
			# 	breakTheEdge(graph, root, child)
			# 	answer += 1
print answer




