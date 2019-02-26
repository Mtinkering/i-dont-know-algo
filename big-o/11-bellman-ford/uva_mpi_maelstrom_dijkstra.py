'''
' Steven Oct 7 2018
' problem: https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 9
' Shortest path, weighted edge
'''
import queue

INF = 10**9


def dijkstra(s, graph, distance):
  pq = queue.PriorityQueue()
  pq.put((0, s))

  distance[s] = 0

  while not pq.empty():
    top = pq.get()

    id = top[1]
    dist = top[0]

    if dist != distance[id]:
      continue

    for neighbor in graph[id]:
      if dist + neighbor[0] < distance[neighbor[1]]:
        distance[neighbor[1]] = dist + neighbor[0]
        pq.put((distance[neighbor[1]], neighbor[1]))


def solve():
  n = int(input())

  graph = [[] for i in range(n)]

  for i in range(n):
    if i == 0:
      continue

    data = input().split()

    for j in range(n):
      if i == j:
        break
      else:
        val = data[j]

        if val != 'x':
          w = int(val)
          graph[i].append((w, j))
          graph[j].append((w, i))
  minTime = [INF for i in range(n)]
  dijkstra(0, graph, minTime)

  return max(minTime)


print(solve())
