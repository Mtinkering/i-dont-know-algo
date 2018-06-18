
def bfs(arr):
  q = Queue()
  visited = [[-1]*len(arr[0]) for i in range(len(arr))]

  q.put((0, 0))

  slickNumber = 1
  if arr[0][0] == 1:
    visited[0][0] = slickNumber
    slickNumber += 1

  neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  while q.empty() == False:
    # print(q.queue)
    i, j = q.get()
    print(i, j)
    area = 0
    # print(arr)
    # print(visited[i][j])
    if arr[i][j] == 1 and visited[i][j] == -1:

      for di, dj in neighbors:
        x = i + di
        y = j + dj

        if 0 <= x < len(arr) and 0 <= y < len(arr[0]):
          area += arr[x][y]

      if area == 0:
        visited[i][j] = slickNumber
        slickNumber += 1
      else:
        if 0 <= i - 1 < len(arr):
          visited[i][j] = visited[i-1][j]

        elif 0 <= j - 1 < len(arr):
          visited[i][j] = visited[i][j-1]

#     elif arr[i][j] == 0:

    for di, dj in neighbors:
      x = i + di
      y = j + dj

      if 0 <= x < len(arr) and 0 <= y < len(arr[0]) and visited[x][y] == -1:
        q.put((x, y))

  return slickNumber


from queue import Queue

n, m = map(int, input().split())

arr = [[]]*n
for i in range(n):
  arr[i] = list(map(int, input().split()))
print(bfs(arr) - 1)
