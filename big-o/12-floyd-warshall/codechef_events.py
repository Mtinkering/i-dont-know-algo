# https://www.codechef.com/problems/MAXCOMP
INF = 10**9


def floydWarshall(graph):
  n = len(graph)

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if graph[i][k] + graph[k][j] > graph[i][j]:
          graph[i][j] = graph[i][k] + graph[k][j]


def solve():
  # Number of events
  m = int(input())

  # Number of hours: 0, 1, 2 -> 48
  n = 49

  graph = [[0]*n for i in range(n)]

  for i in range(n):
    for j in range(n):
      if i > j:
        graph[i][j] = -INF

  for i in range(m):
    u, v, w = map(int, input().split())

    if graph[u][v] < w:
      graph[u][v] = w

#   print(graph)

  floydWarshall(graph)

  maxCompensation = 0
  for i in range(n):
    for j in range(n):
      maxCompensation = max(maxCompensation, graph[i][j])

  print(maxCompensation)


t = int(input())
# 1 ->
for _ in range(t):
  solve()
