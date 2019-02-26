INF = 10**8


def floydWarshall(dist):
  n = len(dist)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if dist[i][j] > dist[i][k] + dist[k][j]:
          dist[i][j] = dist[i][k] + dist[k][j]


def solve(t):

  graph = [[INF]*20 for i in range(20)]

  for i in range(19):
    data = list(map(int, input().split()))

    # zero based
    k = data[0]

    for j in range(k):

      graph[i][data[j+1]-1] = 1
      graph[data[j+1]-1][i] = 1

  floydWarshall(graph)

  print("Test Set #" + str(t))

  for _ in range(int(input())):
    s, d = map(int, input().split())

    minD = graph[s-1][d-1]

    print("%2d to %2d: %d" % (s, d, minD))

  print()


t = 1
while True:
  try:
    solve(t)
    t += 1
  except EOFError:
    break
