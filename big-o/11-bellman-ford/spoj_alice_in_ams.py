import sys
import queue

INF = 10**9


class Scanner:
  def __init__(self, istream):
    self.tokenizer = Scanner.__tokenizer__(istream)

  def __tokenizer__(istream):
    try:
      for line in istream:
        for token in line.strip().split():
          yield token
    except EOFError:
      exit()

  def next(self):
    return self.tokenizer.__next__()


sc = Scanner(sys.stdin)


def BellmanFord(s, n, dist, edges):
  dist[s] = 0

  for i in range(n-1):
    for edge in edges:
      u, v, w = edge

      if dist[u] != INF and dist[u] + w < dist[v]:
        dist[v] = dist[u] + w

  # If a node is relaxed after the n-1 relaxation, it's relaxation must due to cycle
  # A cycle is at most n edge long, so after n more relaxation after the n - 1 th relaxation
  # we should be sure we have found all nodes that can be relaxed by cycles
  for i in range(n):
    for edge in edges:
      u, v, w = edge

      if dist[u] != INF and dist[u] + w < dist[v]:
        if i != n - 1:
          dist[v] = -INF


def solve(n, t):
  names = []
  edges = []
  result = [['']*n for i in range(n)]

  adj = [[] for i in range(n)]

  for i in range(n):
    k = sc.next()
    names.append(k)

    for j in range(n):
      kj = int(sc.next())

      if i != j and kj == 0:
        continue
      else:
        edges.append((i, j, kj))
        adj[i].append(j)

  for s in range(n):
    dist = [INF for i in range(n)]

    BellmanFord(s, n, dist, edges)

    # There is a loop
    for d in range(n):
      if dist[d] == -INF:
        result[s][d] = "NEGATIVE CYCLE"
      elif dist[d] == INF:
        result[s][d] = names[s] + '-' + names[d] + " NOT REACHABLE"
      else:
        result[s][d] = names[s] + '-' + names[d] + ' ' + str(dist[d])

  q = int(sc.next())

  print('Case #' + str(t) + ':')
  for i in range(q):
    s = int(sc.next())
    d = int(sc.next())

    print(result[s][d])


n = int(sc.next())
t = 0
while n != 0:
  t += 1
  solve(n, t)

  n = int(sc.next())
