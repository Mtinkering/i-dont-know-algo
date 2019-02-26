import math
import sys

INF = 10**8


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


def floyWarshall(graph):
  m = len(graph)
  for k in range(m):
    for i in range(m):
      for j in range(m):
        if graph[i][k] + graph[k][j] < graph[i][j]:
          graph[i][j] = graph[i][k] + graph[k][j]


def distance(t1, t2):
  return math.sqrt((t1[0] - t2[0])**2 + (t1[1] - t2[1])**2)


def solve(t):

  n = int(sc.next())

  towns = []
  for i in range(n):
    x = int(sc.next())
    y = int(sc.next())
    towns.append([x, y])

  graph = [[INF]*n for i in range(n)]

  for i in range(n):
    for j in range(n):
      d = distance(towns[i], towns[j])
      if d <= 10:
        graph[i][j] = d

  floyWarshall(graph)

  result = -1
  for i in range(n):
    for j in range(n):
      result = max(result, graph[i][j])

#   print(graph)
  print('Case #%d:' % (t+1))

  if result == INF:
    print('Send Kurdy')
  else:
    print('%.4f' % result)
  print()


n = int(sc.next())

for i in range(n):
  solve(i)
