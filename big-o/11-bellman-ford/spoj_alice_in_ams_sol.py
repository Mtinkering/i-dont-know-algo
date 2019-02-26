MAX = 105
INF = 10 ** 9
dist = [[None] * MAX for _ in range(MAX)]
neg = [[None] * MAX for _ in range(MAX)]


def BellmanFord(s):
  dist[s][s] = 0

  for i in range(n):
    for edge in graph:
      u, v, w = edge

      if dist[s][u] != INF and dist[s][u] + w < dist[s][v]:
        dist[s][v] = dist[s][u] + w
        if i == n - 1:
          neg[s][v] = True


tc = 1

while True:
  n = int(input())
  if n == 0:
    break

  cities = []
  graph = []

  for i in range(n):
    line = input().split()
    cities.append(line.pop(0))

    for j in range(n):
      w = int(line[j])
      dist[i][j] = INF
      neg[i][j] = False

      if i == j:
        w = (-INF if w < 0 else 0)
      if w != 0:
        graph.append((i, j, w))
  print(graph)
  for i in range(n):
    BellmanFord(i)

  q = int(input())
  print("Case #{}:".format(tc))
  tc += 1

  for _ in range(q):
    u, v = map(int, input().split())
    if neg[u][v]:
      print("NEGATIVE CYCLE")
    else:
      print("{}-{} {}".format(cities[u], cities[v], dist[u][v] if dist[u][v] != INF else "NOT REACHABLE"))
