def BellmanFord(s, n, edges, percentage):
  percentage[s] = 1

  for _ in range(n-1):
    for j in range(len(edges)):
      u, v, w = edges[j]

      if percentage[u]*w > percentage[v]:
        percentage[v] = percentage[u]*w


def solve(n, m):
  edges = []

  for _ in range(m):
    a, b, p = map(int, input().split())

    a -= 1
    b -= 1

    edges.append((a, b, p/100))
    edges.append((b, a, p/100))

  percentage = [0 for i in range(n)]

  BellmanFord(0, n, edges, percentage)

  print("{0:.6f}".format(percentage[n-1]*100) + " percent")


data = input().split()

while len(data) != 1:
  solve(int(data[0]), int(data[1]))
  data = input().split()
