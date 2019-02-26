# http: // lightoj.com/volume_showproblem.php?problem = 1012
from queue import Queue


def buildGraph(n, edges):
  graph = [[] for i in range(n)]

  for edge in edges:
    u, v = edge
    graph[u].append(v)
    graph[v].append(u)

  return graph


def bfs(vertex, edges, s):
  graph = buildGraph(vertex, edges)
  visited = [False]*vertex
  n = 1
  q = Queue()
  q.put(s)
  visited[s] = True

  while q.empty() == False:
    u = q.get()
    for v in graph[u]:
      if visited[v] == False:
        visited[v] = True
        q.put(v)
        n += 1
  return n


def numberOfCells():
  w, h = map(int, input().split())
  arr = ['']*h

  for i in range(h):
    arr[i] = input()

  mapping = {}
  edges = []
  vertex = 0
  entryPoint = None

  # Get the vertices and edges
  for i in range(h):
    for j in range(w):
      if arr[i][j] in ['.', '@']:
        if (i, j) not in mapping:
          mapping[(i, j)] = vertex
          vertex += 1

        if j < w-1 and arr[i][j+1] in ['.', '@']:
          if (i, j+1) not in mapping:
            mapping[(i, j+1)] = vertex
            vertex += 1
          u = mapping[(i, j)]
          v = mapping[(i, j+1)]
          edges.append([u, v])

        if i < h-1 and arr[i+1][j] in ['.', '@']:
          if (i+1, j) not in mapping:
            mapping[(i+1, j)] = vertex
            vertex += 1
          u = mapping[(i, j)]
          v = mapping[(i+1, j)]
          edges.append([u, v])

      if arr[i][j] == '@':
        entryPoint = (i, j)

  s = mapping[entryPoint]

  return bfs(vertex, edges, s)


t = int(input())
for i in range(t):
  print('Case ' + str(i+1) + ': ' + str(numberOfCells()))

Complexity:
  # O(V + E) -> V = n * m, E = 4 * n * m
