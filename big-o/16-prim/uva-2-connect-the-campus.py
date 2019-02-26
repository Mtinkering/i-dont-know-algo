# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 9
# Mininum spanning tree

import queue
INF = 10**9


def mst(src, dist, visited, graph):
  pq = queue.PriorityQueue()

  pq.put((0, src))
  dist[src] = 0

  while not pq.empty():
    d, u = pq.get()

    visited[u] = True

    neighbors = graph[u]

    for v in range(len(neighbors)):
      # for w, v in graph[u]:
      w = neighbors[v]

      if visited[v] == False and w < dist[v]:
        dist[v] = w
        pq.put((w, v))


def distance(c1, c2):
  x1, y1 = c1
  x2, y2 = c2

  return ((x2 - x1)**2 + (y2-y1)**2)**0.5


def solve():
  n = int(input())
  coordinates = []

  graph = [[-1]*n for i in range(n)]
  visited = [False]*n
  dist = [INF]*n

  for i in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))

  for i in range(n):
    for j in range(i, n):
      d = distance(coordinates[i], coordinates[j])
      graph[i][j] = d
      graph[j][i] = d

  m = int(input())

  for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1][v - 1] = 0
    graph[v-1][u - 1] = 0

  mst(0, dist, visited, graph)

  ans = 0
  for i in range(n):
    if dist[i] != INF:
      ans += dist[i]
  print('%.2f' % ans)


while True:
  try:
    solve()
  except:
    break
