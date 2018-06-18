
def wallsAndGates(self, rooms):
  """
  :type rooms: List[List[int]]
  :rtype: void Do not return anything, modify rooms in-place instead.
  """
  def bfs(rooms, m, n, q, visited):
    
    # q = Queue()

    # visited[x][y] = True
    # q.put((x, y))

    neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while len(q) != 0:
      nextLevel = []
      for i,j in q:
        for di, dj in neighbors:
          x = di + i
          y = dj + j

          if 0 <= x < m and 0 <= y < n and visited[x][y] == False and rooms[x][y] != -1:
            visited[x][y] = True
            rooms[x][y] = rooms[i][j] + 1
            nextLevel.append((x, y))
      
      q = nextLevel


  
  m = len(rooms)
  if m == 0:
    return

  n = len(rooms[0])
  if n == 0:
    return
  
  zeroes = []
  visited = [[False]*n for i in range(m)]
  for i in range(m):
    for j in range(n):
      if rooms[i][j] == 0:
        zeroes.append((i, j))
        visited[i][j] = True
  bfs(rooms, m, n, zeroes, visited)
  print(rooms)

wallsAndGates(1, [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
                  [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]])
