
def bfs(rooms, m, n, visited, x, y):
	q = [(x,y)]

	visited[x][y] = 0
	# q.put((x, y))

	neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	while len(q) != 0:
		# i, j = q.get()
		nextLevel = []
		for i, j in q:
			for di, dj in neighbors:
				x = di + i
				y = dj + j

				if 0 <= x < m and 0 <= y < n and rooms[x][y] != -1 and rooms[x][y] != 0:
					visited[x][y] = min(visited[x][y], visited[i][j]+1)
					rooms[x][y] = min(rooms[x][y], visited[x][y])
					# q.put((x, y))
					nextLevel.append((x,y))

		q = nextLevel


def wallsAndGates(self, rooms):
		"""
		:type rooms: List[List[int]]
		:rtype: void Do not return anything, modify rooms in-place instead.
		"""
		print(rooms)

		m = len(rooms)
		n = len(rooms[0])
		visited = [[2147483647]*n for i in range(m)]

		for i in range(m):
			for j in range(n):
				if rooms[i][j] == 0 and visited[i][j] == 2147483647:
					bfs(rooms, m, n, visited, i, j)

		print(rooms)
wallsAndGates(1, [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],
               [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]])
