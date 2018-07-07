'''
' Steven Jul 03 2018
' https://www.spoj.com/status/ALLIZWEL,entergmode/
' DFS, BackTracking
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
text = 'ALLIZZWELL'


def isTherePathAt(graph, x, y, idx, cache):
  print(idx, x, y, cache[x][y][idx])
  if cache[x][y][idx] != 0:
    return cache[x][y][idx]

  # Mark to not use in recursion stack
  # visited[x][y] = 1
    # True

  # Check if there is a path with starting A
  neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

  for dx, dy in neighbors:
    i = dx + x
    j = dy + y

    if 0 <= i < len(graph) and 0 <= j < len(graph[0]) and graph[i][j] == text[idx+1]:
      print(i, j, graph[i][j])
      print(idx)
      # Base condition

      if idx == 8:
        print('what')
        cache[i][j][idx] = 2
        return cache[i][j][idx]

      if isTherePathAt(graph, i, j, idx + 1, cache) == 2:
        cache[i][j][idx] = 2
        return cache[i][j][idx]

  print(cache)
  # Reuse the letter
  # visited[x][y] = 0
  cache[x][y][idx] = 1  # False
  print(cache)
  return cache[x][y][idx]


def isTherePath(graph, row, col):
  # Find A's positions
  coordinatesOfA = []
  for i in range(row):
    for j in range(col):
      if graph[i][j] == 'A':
        coordinatesOfA.append((i, j))

  # visited = [[0]*col for i in range(row)]

  # f = [0]  # n * m * 9
  # 0 == not visited
  # 1 == visited but False
  # 2 == visited but True
  cache = [[[0]*9 for j in range(col)] for i in range(row)]

  # Loop through and try for each A
  # If find one, then return True
  for x, y in coordinatesOfA:
    if isTherePathAt(graph, x, y, 0, cache) == 2:
      print('hi')
      return True
  return False


def solve():
  row = int(sc.next())
  col = int(sc.next())

  # Read the matrix
  graph = ['']*row

  for i in range(row):
    graph[i] = sc.next()

  print('YES' if isTherePath(graph, row, col) else 'NO')


t = int(sc.next())
for _ in range(t):
  solve()


8 0 2 0
[[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0,
                                                                                                                         0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]]
[[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]], [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0,
                                                                                                                         0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]]
1 0 L
7
8 1 0 0
2 0 L
8
what
hi
YES

1

3 3
AEL
LWZ
LIZ
# Not possible because it goes from A -> L L I Z Z W E L(L under A) L (2,0)
