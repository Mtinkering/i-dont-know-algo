def bfs(arr, r, c):
  visited = [[False]*c for i in range(r)]
  q = []

  q.append((0, 0))

  visited[0][0] = True

  neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  while len(q) != 0:
    nextLevel = []
    for i, j in q:
      for dx, dy in neighbors:
        x = dx + i
        y = dy + j
        if 0 <= x < r and 0 <= y < c:
          if visited[x][y]:
            visited[x][y] = True
            nextLevel.append((x, y))

          if arr[i][j] == 'S' and arr[x][y] == 'W':
            return 'No'
          if arr[x][y] == '.':
            arr[x][y] = 'D'
    q = nextLevel

  return 'Yes'


r, c = map(int, input().split())
# r = 2
# c = 10
# arr = ['DDDWDDDDDS',
#        'DSDSDDDSDD']
arr = [list(input()) for i in range(r)]
# for i in range(r):
#   arr.append(input().replace('.' ,'D'))

answer = bfs(arr, r, c)

print(answer)
if answer == 'Yes':
  for i in range(r):
    print(''.join(arr[i]))
