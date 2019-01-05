# https: // www.spoj.com/problems/MST/
import queue

INF = 10**9
n, m = map(int, input().split())
graph = [[] for i in range(n)]
visited = [False]*n
dist = [INF]*n


def mst(src, dist, visited):
  pq = queue.PriorityQueue()

  pq.put((0, src))
  dist[src] = 0

  while not pq.empty():
    d, u = pq.get()

    visited[u] = True

    for w, v in graph[u]:
      if visited[v] == False and w < dist[v]:
        dist[v] = w
        pq.put((w, v))


for i in range(m):
  i, j, k = map(int, input().split())

  graph[i-1].append((k, j-1))
  graph[j-1].append((k, i-1))


mst(0, dist, visited)

ans = 0
for i in range(n):
  if dist[i] != INF:
    ans += dist[i]

print(ans)
