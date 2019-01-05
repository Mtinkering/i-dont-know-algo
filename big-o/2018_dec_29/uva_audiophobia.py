import queue

INF = 10**9


def prim(src, des, graph, dist, path):
  pq = queue.PriorityQueue()
  visited = [False]*len(graph)

  dist[src] = 0
  path[src] = -1

  pq.put((0, src))

  while not pq.empty():
    top = pq.get()
    u = top[1]

    if u == des:
      return

    if visited[u]:
      continue

    visited[u] = True

    for w, v in graph[u]:
      if visited[v] == False and dist[v] > w:
        dist[v] = w
        pq.put((w, v))
        path[v] = u


def find_min(src, des, dist, path):
  if des == -1:
    return -1

  if src == des:
    return -1

  d = dist[des]

  parent = path[des]

  d = max(d, find_min(src, parent, dist, path))

  return d


def solve(c, s, q, test):
  graph = {}

  for _ in range(s):
    c1, c2, d = map(lambda x: int(x) - 1, input().split())

    if c1 not in graph:
      graph[c1] = []

    if c2 not in graph:
      graph[c2] = []

    graph[c1].append((d+1, c2))
    graph[c2].append((d+1, c1))

  print("Case #" + str(test))
  for _ in range(q):
    src, des = map(lambda x: int(x) - 1, input().split())

    dist = [INF]*c
    path = [-1]*c

    prim(src, des, graph, dist, path)

    min_sound = find_min(src, des, dist, path)

    if min_sound == INF:
      print("no path")
    else:
      print(min_sound)


test = 0
while True:
  test += 1
  c, s, q = map(int, input().split())
  if c != 0 or s != 0 or q != 0:
    solve(c, s, q, test)
    print()
  else:
    break
