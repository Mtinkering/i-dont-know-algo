'''
' Steven June 20 2018
' https://www.spoj.com/problems/CAM5/
' BFS, DFS
'''

def readInput():
  line = input()
  while not line.strip():
    line = input()
  return line

def dfs(graph, s, visited):
  # Stack
  st = [s]

  visited[s] = True

  while len(st) != 0:
    u = st.pop()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        st.append(v)


# DFS recursion
def dfsr(graph, s, visited):
  visited[s] = True

  for v in graph[s]:
    if not visited[v]:
      dfsr(graph, v, visited)

def bfs(graph, s, visited):
  # Queue
  q = [s]

  visited[s] = True

  while len(q) != 0:
    nextLevel = []
    for u in q:
      for v in graph[u]:
        if not visited[v]:
          visited[v] = True
          nextLevel.append(v)

    q = nextLevel

def solve():
  # Number of peers
  n = int(readInput())

  # Number of edges
  e = int(readInput())

  # Build graph
  graph = [[] for i in range(n)]
  for i in range(e):
    u, v = map(int, readInput().split())
    graph[u].append(v)
    graph[v].append(u)

  # BFS
  visited = [False]*n
  counter = 0
  for i in range(n):
    if not visited[i]:
      dfsr(graph, i, visited)
      counter += 1
  print(counter)

# test cases
t = int(readInput())

for i in range(t):
  solve()
