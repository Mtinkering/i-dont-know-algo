# Start top left
# if all queens are placed (col >= N): return True
# Try all rows in the current colum:
# If it can be placed, mark it. Then from here check if it leads to a solution
# Yes, then return
# No, unmark it. Move on to next row
# Try everything and nothing works, return False
global N
N = 4


def isSafe(board, row, col):
  for i in range(col):
    if board[row][i] == 1:
      return False

  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

    # Check lower diagonal on left side
  for i, j in zip(range(row, N, 1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False

  return True


def solveNQUtil(board, col):
  if col >= N:
    return True

  for i in range(N):
    if isSafe(board, i, col):
      board[i][col] = 1

      if solveNQUtil(board, col + 1) == True:
        return True

      board[i][col] = 0

  return False


def main():
  board = [
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0],
      [0, 0, 0, 0]
  ]

  if solveNQUtil(board, 0) == False:
    print('No solution')
    return False

  # printBoard(board)
  return True


print(main())
