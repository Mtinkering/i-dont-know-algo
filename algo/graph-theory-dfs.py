def dfs(vertex, graph, stack, visited):
  visited[vertex] = True
  for v in graph[vertex]:
    if v not in visited:
      dfs(v, graph, stack, visited)
  stack.append(vertex)

def topologicalSort(graph):
  stack = []
  visited = {}

  for vertex in graph.keys():
    if vertex not in visited:
      dfs(vertex, graph, stack, visited)
  stack.reverse()
  return stack

def buildGraph(n, edges):
  graph = {}

  for edge in edges:
    u, v = edge
    if v not in graph:
      graph[v] = []

    if u in graph:
      graph[u].append(v)
    else:
      graph[u] = [v]
    #graph[v].append(u) directed

  return graph

n, m = map(int, input().split())
edges = []
for edges_i in range(m):
  edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
  edges.append(edges_t)

graph = buildGraph(n, edges)
print(*topologicalSort(graph))
