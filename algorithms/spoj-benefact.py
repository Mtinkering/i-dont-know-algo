'''
' Steven July 7 2018
' https://www.spoj.com/problems/BENEFACT/
' DFS
'''
import sys
sys.setrecursionlimit(1000000)


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


def dfs(graph, src, dist):

  for v, l in graph[src]:
    if dist[v] == float('inf'):
      dist[v] = dist[src] + l
      dfs(graph, v, dist)


def solve():
  n = int(sc.next())
  graph = [[] for i in range(n)]

  for i in range(n-1):
    a = int(sc.next()) - 1
    b = int(sc.next()) - 1
    l = int(sc.next())

    graph[a].append((b, l))
    graph[b].append((a, l))

  answer = 0

  # Each vertex, calculate the maximum
  dist = [float('inf')]*len(graph)
  dist[0] = 0

  dfs(graph, 0, dist)

  m = max(dist)
  v1 = dist.index(m)
#   print(v1)
  dist = [float('inf')]*len(graph)
  dist[v1] = 0

  dfs(graph, v1, dist)

#   print(dist)


#   answer = max(answer, maximumLength)

  print(max(dist))


t = int(sc.next())

for _ in range(t):
  solve()
