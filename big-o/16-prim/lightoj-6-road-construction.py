# http: // lightoj.com/volume_showproblem.php?problem = 1041
import queue

INF = 10**9


def mst(src, graph):
  pq = queue.PriorityQueue()

  visited = set()
  dist = {}
  for v in graph.keys():
    dist[v] = INF

  dist[src] = 0
  pq.put((0, src))

  while not pq.empty():
    top = pq.get()
    u = top[1]

    if u in visited:
      continue

    visited.add(u)

    for w, v in graph[u]:
      if v not in visited and dist[v] > w:
        dist[v] = w
        pq.put((w, v))

  return dist


def solve():
  m = int(input())

  graph = {}
  src = None

  for _ in range(m):

    c1, c2, c = input().split()
    c = int(c)

    if c1 not in graph:
      graph[c1] = []

    if c2 not in graph:
      graph[c2] = []

    src = c1

    graph[c1].append((c, c2))
    graph[c2].append((c, c1))

  dist = mst(src, graph)

  ans = 0
  for d in dist.values():
    if d == INF:
      return 'Impossible'
    else:
      ans += d

  return str(ans)


t = int(input())
for i in range(t):
  input()
  res = solve()
  print("Case " + str(i+1) + ": " + res)
