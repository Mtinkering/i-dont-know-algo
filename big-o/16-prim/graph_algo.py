# 1. Minimum Spanning Tree: Prim's algo
# Purpose: to find the minimum cost to cover all vertex
# https: // stackoverflow.com/questions/20430740/time-complexity-of-prims-algorithm
import queue
INF = 10**9

graph = [[] for i in range(n)]
dist = [INF for i in range(n)]

visited = [False for i in range(n)]

for i in range(m):
  u, v, w = map(int, input().split())

  graph[u].append(Node(v, w))
  graph[v].append(Node(u, w))

prim(0)


def prim(src):
  pq = queue.PriorityQueue()
  pq.put(Node(src, 0))
  dist[src] = 0

  while pq.empty() == False:
    top = pq.get()
    u = top.id
    d = top.dist
    visited[u] = True

    for neighbor in graph[u]:
      v = neighbor.id
      w = neighbor.dist
      if visited[v] == False and w < dist[v]:
        dist[v] = w
        pq.put(Node(v, w))
        path[v] = u

# Tree: n - 1 edges
# O(ElogV)
