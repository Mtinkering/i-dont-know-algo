INF = 10**8


def floydWarshall(graph, m):
  # m[i][j] stores the value of max cost for the feast in that pair i, j
  n = len(graph)

  # Relax l times
  for l in range(n):
    for k in range(n):
      for i in range(n):
        for j in range(n):
          if graph[i][k] != INF and graph[k][j] != INF and graph[i][k] + graph[k][j] + max(m[i][k], m[k][j]) < graph[i][j] + m[i][j]:
            graph[i][j] = graph[i][k] + graph[k][j]
            m[i][j] = max(m[i][k], m[k][j])


def solve(test, c, r, q):
  # read input
  # c # of cities
  # r: number of roads

  graph = [[INF]*c for i in range(c)]
  feast = [[0]*c for i in range(c)]

  cost = list(map(int, input().split()))

  for i in range(r):
    c1, c2, d = map(int, input().split())

    graph[c1-1][c2-1] = d
    graph[c2-1][c1-1] = d

  for i in range(c):
    for j in range(c):
      feast[i][j] = max(cost[i], cost[j])

  # print(feast)

  floydWarshall(graph, feast)

  print('Case #' + str(test))

  for i in range(q):
    s, d = map(int, input().split())
    s -= 1
    d -= 1
    if graph[s][d] != INF:
      print(graph[s][d] + feast[s][d])
    else:
      print(-1)


c, r, q = map(int, input().split())
test = 1
while c != 0 or r != 0 or q != 0:
  solve(test, c, r, q)
  print()
  test += 1
  c, r, q = map(int, input().split())
