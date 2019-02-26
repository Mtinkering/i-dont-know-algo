import queue


def mst(src, graph, visited):
  minCost = 0
  pq = queue.PriorityQueue()

  # dist[src] = 0
  pq.put((0, src))

  while not pq.empty():
    top = pq.get()

    u = top[1]

    if visited[u]:
      continue
    minCost += top[0]

    visited[u] = True

    for w, v in graph[u]:
      if not visited[v]:
        # if not visited[v] and dist[v] > w:
        # dist[v] = w
        pq.put((w, v))

  return minCost


INF = 10**9
t = int(input())

for _ in range(t):
  p = int(input())
  n = int(input())
  m = int(input())

  graph = [[] for i in range(n)]
  for i in range(m):
    a, b, c = map(int, input().split())

    graph[a-1].append((c, b-1))
    graph[b-1].append((c, a-1))

  visited = [False]*n

  # map
  # dist = [INF]*n

  # mst(0, graph, visited, dist)
  d = mst(0, graph, visited)

  # d = 0
  # for i in range(n):
  #   d += dist[i]

  print(d*p)
