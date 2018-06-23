'''
' Steven June 23 2018
' http://codeforces.com/contest/723/problem/D
' BFS, DFS
'''
n, m, k = map(int, input().split())

arr = []

for i in range(n):
  s = list(input())

  arr.append(s)


def dfs(arr, x, y, visited, id):
  st = []

  st.append((x, y))
  visited[x][y] = id
  size = 1

  neighbors = [(0, 1), (0, -1), (-1, 0), (1, 0)]
  isOcean = False

  while len(st) != 0:
    x, y = st.pop()

    # Check if connected to the ocean. But do not stop exploring
    if x == 0 or x == len(arr) - 1 or y == 0 or y == len(arr[0]) - 1:
      isOcean = True

    for di, dj in neighbors:
      i = di + x
      j = dj + y
      if 0 <= i < len(arr) and 0 <= j < len(arr[0]) and visited[i][j] == -1 and arr[i][j] == '.':
        visited[i][j] = id
        st.append((i, j))
        size += 1

  return 0 if isOcean == True else size


visited = [[-1]*m for i in range(n)]
lakes = []
id = 0
for i in range(n):
  for j in range(m):
    if arr[i][j] == '.' and visited[i][j] == -1:
      id += 1
      size = dfs(arr, i, j, visited, id)

      if size > 0:
        lakes.append((size, id))


# Sort the lake by increasing order of size
lakes.sort(key=lambda x: x[0])
toBeFilled = [False] * (id + 1)

minNumberOfCells = 0

for i in range(0, len(lakes) - k, 1):
  lake = lakes[i]
  minNumberOfCells += lake[0]
  toBeFilled[lake[1]] = True

print(minNumberOfCells)

for i in range(n):
  for j in range(m):
    print('*' if visited[i][j] == -1 or toBeFilled[visited[i][j]] else '.', end='')
  print()
