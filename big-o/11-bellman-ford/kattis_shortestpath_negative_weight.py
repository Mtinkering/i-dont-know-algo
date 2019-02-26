INF = 10**9


def BellmanFord(s, n, edges, dist):
  dist[s] = 0

  for i in range(n):
    for j in range(len(edges)):
      u, v, w = edges[j]

      # Reachable from s
      if dist[u] != INF and dist[u] + w < dist[v]:
        if i != n - 1:
          dist[v] = dist[u] + w
        else:
          dist[v] = -INF


def solve(n, m, q, s):

  edges = []

  for _ in range(m):
    u, v, w = map(int, input().split())

    edges.append((u, v, w))

  # Min distance from node s
  dist = [INF for i in range(n)]

  BellmanFord(s, n, edges, dist)

  for i in range(q):
    d = int(input())

    if dist[d] == -INF:
      print('-Infinity')
    elif dist[d] == INF:
      print('Impossible')
    else:
      print(dist[d])


n, m, q, s = map(int, input().split())

while n != 0 or m != 0 or q != 0 or s != 0:
  solve(n, m, q, s)

  n, m, q, s = map(int, input().split())

  if n != 0 or m != 0 or q != 0 or s != 0:
    print()
