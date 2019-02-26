import queue


def dijkstra(src, graph, distance):
  pq = queue.PriorityQueue()
  pq.put((0, src))
  distance[src] = 0

  while not pq.empty():
    w, id = pq.get()

    # This has been in the priority queue, which means the distance has been found
    # Here it is not equal, means this is the second time, means not the shortest.
    # So for sure nothing will fall into the if block
    if w != distance[id]:
      continue

    for neighbor in graph[id]:
      if neighbor[0] + w < distance[neighbor[1]]:
        distance[neighbor[1]] = neighbor[0] + w
        pq.put((distance[neighbor[1]], neighbor[1]))


def solve(n, m):
  source, destination = list(map(int, input().split()))

  graphFromS = [[] for i in range(n)]
  graphFromD = [[] for i in range(n)]

  distFromS = [float('inf') for i in range(n)]
  distFromD = [float('inf') for i in range(n)]

  edges = []

  for _ in range(m):
    u, v, p = list(map(int, input().split()))
    graphFromS[u].append((p, v))
    graphFromD[v].append((p, u))
    edges.append((u, v, p))

  # dijkstra 2 times
  dijkstra(source, graphFromS, distFromS)
  dijkstra(destination, graphFromD, distFromD)

  shortestPath = distFromS[destination]

#   (u, v, w)
#   dist_s[u] + w + dist_t[v] == dist_s[t]

  newGraph = [[] for i in range(n)]
  newDist = [float('inf') for i in range(n)]

  for u, v, p in edges:
    if distFromS[u] + p + distFromD[v] > shortestPath:
      newGraph[u].append((p, v))

  dijkstra(source, newGraph, newDist)

  almostShortestPath = newDist[destination]

  # Go again until there is one path cheaper
#   while almostShortestPath <= shortestPath:
#     # Trace back
#     child = destination
#     parent = thePath[child]

#     # Remove the shortest path
#     while parent != -1:
#       graph[parent] = [t for t in graph[parent] if t[1] != child]
#       child = parent
#       parent = thePath[child]

#     dist = [float('inf') for i in range(n)]
#     thePath = [-1 for i in range(n)]
#     dijkstra(source, destination, graph, dist, thePath)

#     almostShortestPath = dist[destination]

  print(almostShortestPath if almostShortestPath != float('inf') else -1)


0 -> 1, ... n - 2 -> n - 1
0 -> 1
0 ->
)
    0 -> 1: M edges

    M*M*LogE: 10**8


    def main():
    n, m=list(map(int, input().split()))

    while n != 0 and m != 0:
    solve(n, m)

    n, m=list(map(int, input().split()))


    main()
