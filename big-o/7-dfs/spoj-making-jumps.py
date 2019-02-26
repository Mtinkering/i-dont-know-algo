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


def neighbors(r, c):
  return [(r-2, c-1), (r-2, c+1), (r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2), (r+2, c-1), (r+2, c+1)]


def dfs(graph, x, y, counter, total, visited):
  graph[x][y] = counter

  visited['result'] = max(visited['result'], counter)

  if counter == total:
    return True

  for i, j in neighbors(x, y):
    # Reachable, not visited
    if 0 <= i < len(graph) and 0 <= j < 10 and graph[i][j] == 0:
      if dfs(graph, i, j, counter + 1, total, visited) == True:
        return True

  # Backtracking
  graph[x][y] = 0
  return False


def squareUnreached(n):
  row = n

  # -1 is not reachable
  # 0 reachable
  # 1 as visited
  # Calculate reachable but not visited
  arr = [[-1]*10 for i in range(row)]
  total = 0
  for i in range(row):
    offset = int(sc.next())
    col = int(sc.next())
    for j in range(col):
      arr[i][j+offset] = 0
      total += 1

  visited = {'result': 0}

  dfs(arr, 0, 0, 1, total, visited)

  return total - visited['result']


def solve(test, n):
  result = squareUnreached(n)
  print('Case ' + str(test) + ', ' + str(result) + (' square' if result == 1 else ' squares') + ' can not be reached.')


n = int(sc.next())
test = 1
while n != 0:
  solve(test, n)
  test += 1
  n = int(sc.next())
