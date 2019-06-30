
def getNeighbors(x, y):
  return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

# Octaves from the src


def dfs(arr, src, visited, tmp, level, path):
  if level == 8:
    # print(path)
    visited.add(tuple(sorted(path)))
    return

  x, y = src

  # Current exploration
  tmp[x][y] = True
  # res = 0

  for u, v in getNeighbors(x, y):
    if u >= 0 and u < len(arr) and v >= 0 and v < len(arr[0]):

      # Loop
      if tmp[u][v] == True:
        continue

      if arr[u][v] == '.':
        continue

      path.append((u, v))
      dfs(arr, (u, v), visited, tmp, level + 1, path)
      path.pop()

  tmp[x][y] = False


def main():
  t = int(input())
  for _ in range(t):
    n = int(input())

    tmp = [[False]*n for i in range(n)]
    visited = set()

    arr = []
    for i in range(n):
      arr.append(input())

    # ans = 0
    for i in range(n):
      for j in range(n):
        if arr[i][j] == 'X':
          dfs(arr, (i, j), visited, tmp, 1, [(i, j)])

    print(len(visited))

  pass


main()

# bits |= 1 << (sx * n + sy): vi tri do la 1, con lai la giu nguyen
# bits &= ~(1 << (sx * n + sy)): dao nguoc
