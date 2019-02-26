# https: // www.spoj.com/problems/MST/
import queue
INF = 10**9


def prim(src, dist, graph):
  visited = [False]*len(graph)
  pq = queue.PriorityQueue()

  pq.put((0, src))
  # dist[src] = 0
  cost = 0

  while not pq.empty():
    d, u = pq.get()

    # Prevent loop
    if visited[u]:
      continue

    visited[u] = True
    cost += d

    for w, v in graph[u]:
      if visited[v] == False:
        # dist[v] = w
        pq.put((w, v))

  return cost


def main():
  n, m = map(int, input().split())
  graph = [[] for i in range(n)]
  dist = [INF]*n

  for i in range(m):
    i, j, k = map(int, input().split())

    graph[i-1].append((k, j-1))
    graph[j-1].append((k, i-1))

  mst = prim(0, dist, graph)

  # ans = 0
  # for i in range(n):
  #   if dist[i] != INF:
  #     ans += dist[i]

  print(mst)


main()
