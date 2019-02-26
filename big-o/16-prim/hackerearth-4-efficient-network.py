# https: // www.hackerearth.com/challenge/hiring/globalsoft-backend-hiring-challenge/algorithm/efficient-network/
import queue

INF = 10**9

n, m = map(int, input().split())

graph = [[] for i in range(n)]

for i in range(m):
  a, b, l = map(int, input().split())

  graph[a-1].append((l, b-1))
  graph[b-1].append((l, a-1))


dist = [INF]*n
visited = [False]*n


def mst(src, graph, visited, dist):
  pq = queue.PriorityQueue()

  pq.put((0, src))
  dist[src] = 0

  while not pq.empty():
    w, u = pq.get()
    visited[u] = True

    for d, v in graph[u]:
      if visited[v] == False and dist[v] > d:
        dist[v] = d
        pq.put((d, v))


mst(0, graph, visited, dist)

q = int(input())
ans = 0

if q != 0:
  arr = list(map(int, input().split()))
  arr.sort()

  dist.sort(reverse=True)

  j = 0
  for i in range(n):
    if j < q:
      ans += min(arr[j], dist[i])  # arr[j] > dist[i], => arr[j] > dist[i+1]....
      j += 1
    else:
      ans += dist[i]
else:
  for i in range(n):
    if dist[i] != INF:
      ans += dist[i]
print(ans)

# prim's algo
# ElogV
