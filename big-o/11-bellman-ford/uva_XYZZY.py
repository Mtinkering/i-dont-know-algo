
import queue


def hasPath(source, destination, graph):
  q = queue.Queue()

  visited = [False for i in range(len(graph))]

  q.put(source)
  visited[source] = True

  while not q.empty():
    u = q.get()

    if u == destination:
      return True

    for v in graph[u]:
      if visited[v] == False:
        visited[v] = True
        q.put(v)

  return False


def BellmanFordShortestPath(s, graph, dist, n, d, graphBFS):
  dist[s] = 100

  for i in range(n):
    for j in range(len(graph)):
      u, v, w = graph[j]

      if dist[u] > 0 and dist[u] + w > dist[v]:
        if i == n - 1:
          # u, v in a positive cycle
          # Check if d is reachable from u, ignore the weight
          # This will go through all the vertices
          if hasPath(u, d, graphBFS):
            # winnable
            return True
#           else:
#             return False
        else:
          dist[v] = dist[u] + w

  # no cycle, and we have the maximum for all rooms reachable from s
  return dist[d] > 0

#  blah blah
# -79 0
# -15 7 24 34 1 15 30 22 4
# 66 9 7 27 26 7 21 9 18 28 32
# 0 7 19 35 26 26 11 31 5

# 55 .  n
# 0 8 39 14 7 53 21 38 7 46


def solve(n):
  energies = [0 for i in range(n)]

  edges = []
  adj = [[] for i in range(n)]  # [[2,3,4,], [1,2,3]]

  for i in range(n):
    data = list(map(int, input().split()))

    energies[i] = data.pop(0)

    if len(data) == 0:
      data = list(map(int, input().split()))

    doors = data.pop(0)

    while len(data) < doors:
      data.extend(list(map(int, input().split())))

    for target in data:
      target -= 1

      edges.append([i, target, 0])

      # Graph for BFS
      adj[i].append(target)

  for edge in edges:
    # Adjust the weight
    edge[2] = energies[edge[1]]

  s = 0
  d = n - 1

  # dist[u] means the maximum energy that we can have in room u
  dist = [0 for i in range(n)]

  res = BellmanFordShortestPath(s, edges, dist, n, d, adj)

  print('winnable') if res == True else print('hopeless')


n = int(input())

while (n != -1):
  solve(n)

  n = int(input())
