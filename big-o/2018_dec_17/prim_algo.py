import queue


def prim(src, g):
  pq = queue.PriorityQueue()
  pq.put((0, src))

  visited = [False]*len(g)
  min_cost = 0

  while not pq.empty():
    d, u = pq.get()

    # Prevent loop
    if visited[u]:
      continue

    visited[u] = True

    min_cost += d

    for w, v in g[u]:
      if visited[v] == False:
        pq.put((w, v))

  return min_cost


def main():
  n, m = map(int, input().split())
  graph = [[] for i in range(n)]

  for i in range(m):
    a, b, w = map(lambda x: int(x) - 1, input().split())

    w += 1

    graph[a].append((w, b))
    graph[b].append((w, a))

  d = prim(0, graph)
  print(d)


main()
