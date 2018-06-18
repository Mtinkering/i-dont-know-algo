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
  path = [-1]*vertex
  q = Queue()
  q.put(s)
  visited[s] = True
 
  while q.empty() == False:
    u = q.get()
    for v in graph[u]:
      if visited[v] == False:
        visited[v] = True
        q.put(v)
        path[v] = u
 
  return path
 
def isMazeValid():
  m, n = map(int, input().split())
  arr = ['']*m
 
  for i in range(m):
    arr[i] = input()
 
  entryPoint = None
  exitPoint = None
 
  # Check if more than 2 entry + exit points
  counter = 0
  for i in range(0, m):
    for j in range(0, n):
      if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and arr[i][j] == '.':
        counter += 1
        if entryPoint == None:
          entryPoint = (i, j)
        else:
          exitPoint = (i, j)
 
  if counter != 2:
    return 'invalid'
 
  mapping = {}
  edges = []
  vertex = 0
 
  # Get the edges
  for i in range(0, m):
    for j in range(0, n):
      if arr[i][j] == '.':
        if (i, j) not in mapping:
          mapping[(i, j)] = vertex
          vertex += 1
        
        if j < n-1 and arr[i][j+1] == '.':
          if (i, j+1) not in mapping:
            mapping[(i, j+1)] = vertex
            vertex += 1
          u = mapping[(i,j)]
          v = mapping[(i, j+1)]
          edges.append([u,v])
      
        if i < m-1 and arr[i+1][j] == '.':
          if (i+1, j) not in mapping:
            mapping[(i+1, j)] = vertex
            vertex += 1
          u = mapping[(i, j)]
          v = mapping[(i+1, j)]
          edges.append([u, v])
 
  s  = mapping[entryPoint]
  f = mapping[exitPoint]
  path = bfs(vertex, edges, s)
 
  if path[f] != -1:
    return 'valid'
  else:
    return 'invalid'
 
t = int(input())
for _ in range(t):
  print(isMazeValid())


# Efficient solution
from queue import Queue


def bfs(maze, x, y):
  q = Queue()
  q.put((x, y))
  visited = [[False]*len(maze[0]) for i in range(len(maze))]

  visited[x][y] = True
  DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  while not q.empty():
    x, y = q.get()
    for dx, dy in DIR:
      new_x, new_y = x + dx, y + dy
      if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and not visited[new_x][new_y] and maze[new_x][new_y] == '.':
        visited[new_x][new_y] = True
        q.put((new_x, new_y))

  return visited


def isMazeValid():
  m, n = map(int, input().split())
  arr = ['']*m

  for i in range(m):
    arr[i] = input()

  entryPoint = None
  exitPoint = None

  # Check if more than 2 entry + exit points
  counter = 0
  for i in range(0, m):
    for j in range(0, n):
      if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and arr[i][j] == '.':
        counter += 1
        if entryPoint == None:
          entryPoint = (i, j)
        else:
          exitPoint = (i, j)

  if counter != 2:
    return 'invalid'

  visited = bfs(arr, entryPoint[0], entryPoint[1])

  if visited[exitPoint[0]][exitPoint[1]]:
    return 'valid'
  else:
    return 'invalid'


t = int(input())
for _ in range(t):
  print(isMazeValid())

# (i, j) -> (i + 1, j + 0), (i - 1, j + 0), (i + 0, j + 1), (i + 0, j - 1)

#
