n, m = map(int, input().split())

arr = [None]*n

for i in range(n):
  arr[i] = list(input())

r1, c1 = map(lambda x: int(x) - 1, input().split())
r2, c2 = map(lambda x: int(x) - 1, input().split())


def bfs(maze, x, y, r2, c2):
  q = [(x, y)]
  path = [[None]*len(maze[0]) for i in range(len(maze))]

  path[x][y] = (x, y)
  DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  while len(q) != 0:
    nextLevel = []

    for x, y in q:
      for dx, dy in DIR:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and path[new_x][new_y] == None and maze[new_x][new_y] == '.':
          path[new_x][new_y] = (x, y)
          nextLevel.append((new_x, new_y))

        # When maze[r2][c2] == 'X'
        if new_x == r2 and new_y == c2 and path[new_x][new_y] == None:
          path[new_x][new_y] = (x, y)
          nextLevel.append((new_x, new_y))

    q = nextLevel
  return path


def printPath(arr, path, sx, sy, fx, fy):
  b = []

  while True:
    b.append((fx, fy))
    (fx, fy) = path[fx][fy]
    if fx == sx and fy == sy:
      break

  # Crack the ice that we went through
  for i in range(len(b)-1, -1, -1):
    u, v = b[i]
    arr[u][v] = 'X'


path = bfs(arr, r1, c1, r2, c2)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# print(path)
answer = 'NO'

if n == 1 and m == 1:
  answer = 'NO'
elif r1 == r2 and c1 == c2:
  for dx, dy in directions:
    new_x, new_y = r2 + dx, c2 + dy

    if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][new_y] == '.':
      answer = 'YES'
      break
elif path[r2][c2] != None:
  if arr[r2][c2] == 'X':
    answer = 'YES'

  else:
    printPath(arr, path, r1, c1, r2, c2)

    for dx, dy in directions:
      new_x, new_y = r2 + dx, c2 + dy

      if 0 <= new_x < n and 0 <= new_y < m and arr[new_x][new_y] == '.':
        answer = 'YES'
        break

print(answer)
