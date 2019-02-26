'''
' Steven Oct 7 2018
' problem: https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 9
' Shortest path, weighted edge
'''

INF = 10**9


def bellmanFord(s, n, edges, minTime):
  minTime[s] = 0

  for _ in range(n-1):
    for j in range(len(edges)):
      u, v, w = edges[j]

      if minTime[u] != INF and minTime[u] + w < minTime[v]:
        minTime[v] = minTime[u] + w


def solve():
  n = int(input())

  edges = []

  for i in range(n):
    if i == 0:
      continue

    data = input().split()

    for j in range(n):
      if i == j:
        break
      else:
        val = data[j]

        if val != 'x':
          edges.append((i, j, int(val)))
          edges.append((j, i, int(val)))

  minTime = [INF for i in range(n)]
  bellmanFord(0, n, edges, minTime)

  return max(minTime)


print(solve())
