import queue


class Node:
  def __init__(self, id, w):
    self.id = id
    self.w = w

  def __lt__(self, other):
    return self.w <= other.w


def dijkstra(s, graph, dist):
  dist[s] = 0
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))

  while not pq.empty():
    top = pq.get()
    u = top.id
    w = top.w

    if w != dist[u]:
      continue

    for neighbor in graph[u]:
      if neighbor.w + w < dist[neighbor.id]:
        dist[neighbor.id] = neighbor.w + w
        pq.put(Node(neighbor.id, dist[neighbor.id]))


def solve():
  n, m, k, s, t = list(map(int, input().split()))
  s = s - 1
  t = t - 1

  graphFromS = [[] for i in range(n)]
  graphFromT = [[] for i in range(n)]
  distFromS = [float('inf') for i in range(n)]
  distFromT = [float('inf') for i in range(n)]

  for i in range(m):
    d, c, l = list(map(int, input().split()))
    graphFromS[d-1].append(Node(c-1, l))
    graphFromT[c-1].append(Node(d-1, l))

  dijkstra(s, graphFromS, distFromS)
  dijkstra(t, graphFromT, distFromT)

  proposals = []
  for _ in range(k):
    u, v, q = list(map(int, input().split()))
    proposals.append((u-1, v-1, q))

  #   s -> u -> v -> t # road 1
  #   s -> v -> u -> t # road 2
  #   s -> x.... -> t
#   k * ElogV
  # Orignal
  answer = distFromS[t]

  for p in proposals:
    path1 = distFromS[p[0]] + p[2] + distFromT[p[1]]
    path2 = distFromS[p[1]] + p[2] + distFromT[p[0]]

    answer = min(answer, path1, path2)

  return answer

#   u -> v:

#   s -> u: exists
#   v -> t: not

#   => s -> u -> v # -> t


t = int(input())

for case in range(t):
  result = solve()
  print(-1 if result == float("inf") else result)
