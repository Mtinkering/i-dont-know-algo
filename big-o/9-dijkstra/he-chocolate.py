'''
 ' Created by steven.
 ' Date: 25/8/18
 ' Problem: https: // www.hackerearth.com/practice/algorithms/graphs/shortest-path-algorithms/practice-problems/algorithm/successful-marathon-0691ec04/description/
 ' Tags: dijkstra
 ' Algo: 
 ' TimeComplexity: ElogV
 ' SpaceComplexity:
'''

import queue


# class Node:
#   def __init__(self, id, dist):
#     self.id = id
#     self.dist = dist

#   def __lt__(self, other):
#     return self.dist <= other.dist


def dijkstra(s, graph, distance):
  pq = queue.PriorityQueue()
  pq.put((0, s))
  distance[s] = 0

  while not pq.empty():
    top = pq.get()
    id = top[1]
    dist = top[0]

    # Remove duplicate
    if dist != distance[id]:
      continue

    for neighbor in graph[id]:
      # cost from source to id plus id -> neighbor <
      if dist + neighbor[0] < distance[neighbor[1]]:
        distance[neighbor[1]] = dist + neighbor[0]
        pq.put((dist + neighbor[0], neighbor[1]))


n, m, k, x = list(map(int, input().split()))
graph = [[] for i in range(n)]

cities = list(map(lambda x: int(x) - 1, input().split()))

for i in range(m):
  u, v, d = list(map(int, input().split()))

  graph[u-1].append((d, v-1))
  graph[v-1].append((d, u-1))


friend, you = list(map(lambda x: int(x) - 1, input().split()))
friendToChocolate = [float('inf') for i in range(n)]
chocolateToYou = [float('inf') for i in range(n)]

dijkstra(friend, graph, friendToChocolate)
dijkstra(you, graph, chocolateToYou)


minDistance = float('inf')

for city in cities:
  if chocolateToYou[city] <= x and friendToChocolate[city] != float('inf'):
    distance = friendToChocolate[city] + chocolateToYou[city]
    minDistance = min(minDistance, distance)

print(-1 if minDistance == float('inf') else minDistance)
