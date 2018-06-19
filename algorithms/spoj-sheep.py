'''
' Steven June 19 2018
' https://www.spoj.com/problems/KOZE/
' BFS
'''

from queue import Queue

def bfs(arr, x, y, visited):
  sheep = 0
  wolves = 0
  isConnectedToBackyard = False
  q = Queue()

  q.put((x, y))
  neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  while not q.empty():
    i, j = q.get()

    # Only process it if it has not been visited
    if visited[i][j] == True:
      continue
    visited[i][j] = True
    if arr[i][j] == 'k':
      sheep += 1
    elif arr[i][j] == 'v':
      wolves += 1

    if i == 0 or i == len(arr) - 1 or j == 0 or j == len(arr[0]) - 1:
      isConnectedToBackyard = True

    for dx, dy in neighbors:
      x = dx + i
      y = dy + j

      if 0 <= x < len(arr) and 0 <= y < len(arr[0]) and not visited[x][y] and arr[x][y] in ['k', 'v', '.']:
        q.put((x, y))

  return (sheep, wolves, isConnectedToBackyard)


# Prevent reading empty line
line = input()
while not line.strip():
  line = input()

n, m = map(int, line.strip().split())

arr = []
for i in range(n):
  s = input()
  while not s.strip():
    s = input()

  arr.append(s.strip())


totalSheep = 0
totalWolves = 0
visited = [[False]*m for i in range(n)]
for i in range(n):
  for j in range(m):
    if arr[i][j] in ['k', 'v'] and visited[i][j] == False:
      sheep, wolves, isConnectedToBackyard = bfs(arr, i, j, visited)

      # 3 conditions as described
      if isConnectedToBackyard == True:
        totalSheep += sheep
        totalWolves += wolves
      elif sheep > wolves:
        totalSheep += sheep
      else:
        totalWolves += wolves

print(totalSheep, totalWolves)
