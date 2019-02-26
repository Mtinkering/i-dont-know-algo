# https: // www.spoj.com/problems/SOCIALNE/
# O(n^3)


def floyWarshall(dist):
  m = len(dist)

  for k in range(m):
    for i in range(m):
      for j in range(m):
        if dist[i][k] + dist[k][j] < dist[i][j]:
          dist[i][j] = dist[i][k] + dist[k][j]


INF = 10**8


def solve():
  s = input()
  m = len(s)

  matrix = [s]

  for i in range(m-1):
    s = input()
    matrix.append(s)

  dist = [[INF]*m for _ in range(m)]

  for i in range(m):
    for j in range(m):
      if matrix[i][j] == 'Y':
        dist[i][j] = 1

  floyWarshall(dist)

  id = 0
  mostFriend = 0

  for i in range(m):
    counter = 0

    for j in range(m):
      if i == j:
        continue
      else:
        # A possible friend
        if dist[i][j] == 2:
          counter += 1

    if counter > mostFriend:
      mostFriend = counter
      id = i

  print(id, mostFriend)


t = int(input())

for _ in range(t):
  solve()
