# http: // www.lightoj.com/volume_showproblem.php?problem = 1074
INF = 10 ** 9


def BellmanFord(s, n, dist, graph):
  dist[s] = 0
  m = len(graph)

  for i in range(n):
    for u, v, w in graph:
      # No need inf check? because it is limited to 1B
      if dist[u] != INF and dist[u] + w < dist[v]:
        if i == n - 1:
          return False
        else:
          dist[v] = dist[u] + w

  return True


def solve(testCase):
  input()

  n = int(input().strip())
  busyness = list(map(int, input().strip().split()))

  m = int(input().strip())  # roads
  graph = []
  for i in range(m):
    source, destination = map(int, input().strip().split())

    # To zero index
    source -= 1
    destination -= 1

    weight = (busyness[destination] - busyness[source])**3

    graph.append((source, destination, weight))

  s = 0
  dist = [INF for i in range(n)]

  res = BellmanFord(s, n, dist, graph)

  print("Case " + str(testCase + 1) + ":")
  queries = int(input().strip())

  for i in range(queries):
    q = int(input().strip()) - 1  # To zero index

    # Res must be True to have some meaning about the dist[q]
    if res == False or dist[q] == INF or dist[q] < 3:
      print("?")
    else:
      print(dist[q])


t = int(input().strip())

for i in range(t):
  solve(i)
