def check(board, row, col):
  for i in range(row):
    if board[i][col]:
      return False

  i = row
  j = col
  while i >= 0 and j >= 0:
    if board[i][j]:
      return False

    i -= 1
    j -= 1

  i = row
  j = col
  while j < N and i >= 0:
    if board[i][j]:
      return False

    i -= 1
    j += 1

  return True


def nQueen(board, row, N):
  if row == N:
    printSolution()
    return True

  for j in range(N):
    if check(board, row, j) == True:
      board[row][j] = 1
      nQueen(board, row + 1, N)
      board[row][j] = 0

  return False


def main():
  N = 4
  board = [[0]*N for i in range(N)]

  nQueen(board, 0, N)


main()
