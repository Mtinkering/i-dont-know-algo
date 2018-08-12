'''
 * Created by steven.
 * Date: 13/8/18
 * Problem: http: // www.lightoj.com/volume_showproblem.php?problem = 1174
 * Tags: dijkstra
 * Algo: min distance is the max total time of min from s to i, plus min from i to d, for all i in between s and d.
 * Complexity: ElogV, with V is number of vertices, E is the number of edges
'''

import queue


class Node:
  def __init__(self, id, w):
    self.id = id
    self.w = w

  def __lt__(self, other):
    return self.w <= other.w


def dijkstra(s, graph, dist):
  dist[s] = 0
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))

  while not pq.empty():
    top = pq.get()
    u = top.id
    w = top.w

    for neighbor in graph[u]:
      if neighbor.w + w < dist[neighbor.id]:
        dist[neighbor.id] = neighbor.w + w
        pq.put(Node(neighbor.id, dist[neighbor.id]))


def solve():
  n = int(input())
  r = int(input())
  graph = [[] for i in range(n)]

  for i in range(r):
    u, v = list(map(int, input().split()))
    graph[u].append(Node(v, 1))
    graph[v].append(Node(u, 1))

  s, d = list(map(int, input().split()))

  # Calculate s -> i
  # Calcualte d -> i
  # Sum and take the max
  distFromS = [float('inf') for i in range(n)]
  distFromD = [float('inf') for i in range(n)]
  dijkstra(s, graph, distFromS)
  dijkstra(d, graph, distFromD)

  total = 0
  for index, value in enumerate(distFromS):
    distance = value + distFromD[index]
    total = max(total, distance)

  return total


t = int(input())

for case in range(t):
  result = solve()
  print("Case " + str(case + 1) + ": " + str(result))
