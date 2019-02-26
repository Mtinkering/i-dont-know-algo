n = 5
import sys
sys.setrecursionlimit(1000000)


def isSafe(x, y, board):
  return 0 <= x < n and 0 <= y < n and board[x][y] == -1


def neighbors(r, c):
  return [(r-2, c-1), (r-2, c+1), (r-1, c-2), (r-1, c+2), (r+1, c-2), (r+1, c+2), (r+2, c-1), (r+2, c+1)]


def solveKTUtil(x, y, counter, board):
  # Here means we reached n*n - 1 which is the total
  if counter == n*n:
    return True

  for nextX, nextY in neighbors(x, y):
    if 0 <= nextX < n and 0 <= nextY < n and board[nextX][nextY] == -1:
      board[nextX][nextY] = counter
      if solveKTUtil(nextX, nextY, counter + 1, board) == True:
        return True
      else:
        board[nextX][nextY] = -1
  return False


def solveKT():
  board = [[-1]*n for i in range(n)]

  for i in range(n):
    print(*board[i])
  print()

  board[0][0] = 0

  if not solveKTUtil(0, 0, 1, board):
    print('not exist')
    return False
  else:
    for i in range(n):
      print(*board[i])
    print()
    return True


solveKT()
