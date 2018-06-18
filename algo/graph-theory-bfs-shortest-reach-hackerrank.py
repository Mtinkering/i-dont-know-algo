def buildGraph(n, edges):
  graph = {}
  for i in range(n):
    graph[i + 1] = []
  
  for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)
  
  return graph

def bfs(n, m, edges, s):
  graph = buildGraph(n, edges)
  frontier = [s]
  level = 1
  visited = {s: 0}
  
  while len(frontier) != 0:
    nextToVisit = []
    for u in frontier:
      for v in graph[u]:
        if v not in visited:
          visited[v] = level
          nextToVisit.append(v)
    level += 1
    frontier = nextToVisit
  
  result = []
  for i in range(n):
    if (i+1 != s):
      if (i+1 not in visited):
        result.append(-1)
      else:
        result.append(visited[i+1]*6)
    
  return result


q = int(input().strip())
for a0 in range(q):
  n, m = input().strip().split(' ')
  n, m = [int(n), int(m)]
  edges = []
  for edges_i in range(m):
    edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
    edges.append(edges_t)
  s = int(input().strip())
  result = bfs(n, m, edges, s)
  print (" ".join(map(str, result)))
