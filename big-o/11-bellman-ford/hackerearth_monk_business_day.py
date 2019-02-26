import queue

INF = 10**9


def hasPath(s, d, adj):
  visited = [False for i in range(len(adj))]

  visited[s] = True
  q = queue.Queue()
  q.put(s)

  while not q.empty():
    u = q.get()

    if u == d:
      return True

    for v in adj[u]:
      if visited[v] == False:
        visited[v] = True
        q.put(v)

  return False


def BellmanFord(s, n, m, edges, money, adj):
  money[s] = 0

  for i in range(n):
    for j in range(m):
      u, v, w = edges[j]

      if money[u] + w > money[v]:
        if i == n - 1:
          # Reachable from s
          if hasPath(s, v, adj):
            return True
        else:
          money[v] = money[u] + w

  return False


def solve():
  n, m = map(int, input().split())

  edges = []
  adj = [[] for i in range(n)]

  for _ in range(m):
    i, j, c = map(int, input().split())

    # zero based
    i -= 1
    j -= 1

    edges.append((i, j, c))
    adj[i].append(j)

  # The maximum money when trading item i
  money = [0 for i in range(n)]

  res = BellmanFord(0, n, m, edges, money, adj)

  if res == True:
    print('Yes')
  else:
    print('No')


t = int(input())

for _ in range(t):
  solve()

