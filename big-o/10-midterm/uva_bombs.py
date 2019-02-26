# import queue


# def inRange(x, y, arr):
#   return 0 <= x < len(arr) and 0 <= y < len(arr[0])


# def getNeighbors(x, y):
#   return [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]


def bfs(source, destination, matrix):
  # q = queue.Queue()
  q = [source]
  # q.put(source)

  matrix[source[0]][source[1]] = 1

  neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  while len(q) != 0:
    nextLevel = []

    for r, c in q:
      # r, c = q.get()

      if r == destination[0] and c == destination[1]:
        break
      for dx, dy in neighbors:
        x = dx + r
        y = dy + c
        if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 0:
          # q.put((x, y))
          nextLevel.append((x, y))
          matrix[x][y] = matrix[r][c] + 1

    q = nextLevel
  # 0: not visited
  # -1: mine
  # 1+: distance


def solve(r, c):
  matrix = [[0]*c for i in range(r)]

  rows = int(input())

  for _ in range(rows):
    data = list(map(int, input().split()))

    rowNumber = data[0]  # index 0
    numberOfBombs = data[1]

    for j in range(numberOfBombs):
      col = data[j+2]
      matrix[rowNumber][col] = -1
  sx, sy = map(int, input().split())
  dx, dy = map(int, input().split())

  bfs((sx, sy), (dx, dy), matrix)

  return matrix[dx][dy] - 1


r, c = map(int, input().split())

while r != 0 and c != 0:
  print(solve(r, c))
  r, c = map(int, input().split())
