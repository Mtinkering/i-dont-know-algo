n = 5


def neighbors(r, c):
  return [(r-2, c-1), (r-2, c+1), (r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2), (r+2, c-1), (r+2, c+1)]


def dfs(board, x, y, counter):
  board[x][y] = counter

  if counter == n*n-1:
    return True

  for i, j in neighbors(x, y):
    if 0 <= i < n and 0 <= j < n and board[i][j] == -1:
      if dfs(board, i, j, counter + 1) == True:
        return True

  # Backtracking
  board[x][y] = -1
  return False


board = [[-1]*n for i in range(n)]

print(dfs(board, 0, 0, 0))
for i in range(n):
  print(*board[i])
