
# This solution is better because it's easier to understand

INF = 10**9


def BellmanFordShortestPath(s, graph, dist, n):
  dist[s] = 100

  for _ in range(n-1):
    for j in range(len(graph)):
      u, v, w = graph[j]

      if dist[u] > 0 and dist[u] + w > dist[v]:
        dist[v] = dist[u] + w

  # If a node is relaxed after the n-1 relaxation, it's relaxation must due to cycle
  # A cycle is at most n edge long, so after n more relaxation after the n - 1 th relaxation
  # we should be sure we have found all nodes that can be relaxed by cycles
  for i in range(n):
    for j in range(len(graph)):
      u, v, w = graph[j]

      if dist[u] > 0 and dist[u] + w > dist[v]:
        dist[v] = INF


def solve(n):
  energies = [0 for i in range(n)]

  edges = []

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

  for edge in edges:
    # Adjust the weight
    edge[2] = energies[edge[1]]

  s = 0
  d = n - 1

  # dist[u] means the maximum energy that we can have in room u
  dist = [0 for i in range(n)]

  BellmanFordShortestPath(s, edges, dist, n)

  print('winnable') if dist[d] > 0 else print('hopeless')


n = int(input())

while (n != -1):
  solve(n)

  n = int(input())
