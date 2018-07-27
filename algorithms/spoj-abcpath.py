'''
' Steven July 2 2018
' https://www.spoj.com/problems/ABCPATH/
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


def dfs(arr, visited, position, target, counter, result):
  result['maxL'] = max(result['maxL'], counter)

  total = len(arr)*len(arr[0])
  if counter == total:
    return True

  x, y = position
  visited[x][y] = counter
  for i in range(len(visited)):
    print(*visited[i])
  print()
  neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for dx, dy in neighbors:
    i = dx + x
    j = dy + y
    if 0 <= i < len(arr) and 0 <= j < len(arr[0]) and visited[i][j] == -1:
      if arr[i][j] == target:
        nextTarget = chr(ord(target) + 1)
        if target == 'Z':
          nextTarget = 'A'
        if dfs(arr, visited, (i, j), nextTarget, counter + 1, result) == True:
          return True

  # Backtracking
  visited[x][y] = -1
  return False


def longestPath(arr):

  visited = [[-1]*w for i in range(h)]
  # -1 not visited
  # 0 visiting
  # 1 visited

  positionsOfA = []

  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j] == 'A':
        # Track the indices
        positionsOfA.append((i, j))

  # Start from A
  maxLength = 0
  result = {'maxL': 0}
  for position in positionsOfA:
    dfs(arr, visited, position, 'B', 1, result)
    maxLength = max(maxLength, result['maxL'])
  return maxLength


def solve(h, w, t):
  arr = []
  for _ in range(h):
    row = list(sc.next())
    arr.append(row)

  result = longestPath(arr)

  print('Case ' + str(t) + ': ' + str(result))


sc = Scanner(sys.stdin)

h = int(sc.next())
w = int(sc.next())
testCase = 1

while h != 0 and w != 0:
  solve(h, w, testCase)
  testCase += 1
  h = int(sc.next())
  w = int(sc.next())


== == Fix == ==

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


def dfs(arr, position, cache):
  x, y = position
  if cache[x][y] != 0:
    return cache[x][y]
#   result['maxL'] = max(result['maxL'], counter)

#   total = len(arr)*len(arr[0])
#   if counter == total:
#     return True


#   visited[x][y] = counter

#   for i in range(len(visited)):
#     print(*visited[i])
#   print()

  neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  result = 1
  for dx, dy in neighbors:
    i = dx + x
    j = dy + y
    if 0 <= i < len(arr) and 0 <= j < len(arr[0]):
      if arr[i][j] == chr(ord(arr[x][y]) + 1):
        #         nextTarget = chr(ord(target) + 1)
        #         if target == 'Z':
        #           nextTarget = 'A'
        result = max(result, dfs(arr, (i, j), cache) + 1)

  # Backtracking
#   visited[x][y] = -1
  cache[x][y] = result
  return result


def longestPath(arr):

  #   visited = [[-1]*w for i in range(h)]
  # -1 not visited
  # 0 visiting
  # 1 visited

  positionsOfA = []

  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if arr[i][j] == 'A':
        # Track the indices
        positionsOfA.append((i, j))

  # Start from A
  maxLength = 0
#   result = {'maxL': 0}
  cache = [[0] * len(arr[0]) for i in range(len(arr))]
  for position in positionsOfA:
    result = dfs(arr, position, cache)
    maxLength = max(maxLength, result)
  return maxLength


def solve(h, w, t):
  arr = []
  for _ in range(h):
    row = list(sc.next())
    arr.append(row)

  result = longestPath(arr)

  print('Case ' + str(t) + ': ' + str(result))


sc = Scanner(sys.stdin)

h = int(sc.next())
w = int(sc.next())
testCase = 1

while h != 0 and w != 0:
  solve(h, w, testCase)
  testCase += 1
  h = int(sc.next())
  w = int(sc.next())
