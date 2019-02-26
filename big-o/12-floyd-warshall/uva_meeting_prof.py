import queue

INF = 10**8


def dijkstra(graph, s, dist):
  pq = queue.PriorityQueue()

  pq.put((0, s))
  dist[s] = 0

  while not pq.empty():
    top = pq.get()

    d = top[0]
    u = top[1]

    for neighbor in graph[u]:
      w = neighbor[0]
      v = neighbor[1]

      if w + d < dist[v]:
        dist[v] = w + d
        pq.put((w+d, v))


def toZeroBasedVertex(letter):
  return ord(letter) - ord('A')


def solve(m):
  n = 26

  graphForYoung = [[] for i in range(n)]
  graphForAged = [[] for i in range(n)]

  for _ in range(m):
    edge = input().split()
    u = toZeroBasedVertex(edge[2])
    v = toZeroBasedVertex(edge[3])
    w = int(edge[4])

    if edge[0] == 'Y':
      graphForYoung[u].append((w, v))
      if edge[1] != 'U':
        graphForYoung[v].append((w, u))
    else:
      graphForAged[u].append((w, v))
      if edge[1] != 'U':
        graphForAged[v].append((w, u))

  s, d = map(toZeroBasedVertex, input().split())

  distForYoung = [INF for i in range(n)]
  distForAged = [INF for i in range(n)]

  dijkstra(graphForYoung, s, distForYoung)
  dijkstra(graphForAged, d, distForAged)

  result = []
  currentMin = INF
  for i in range(n):
    # If ther is a place connecting them
    placeName = chr(i + ord('A'))
    if distForYoung[i] != INF and distForAged[i] != INF:
      if distForYoung[i] + distForAged[i] == currentMin:
        result.append(placeName)
      elif distForYoung[i] + distForAged[i] < currentMin:
        currentMin = distForYoung[i] + distForAged[i]
        result = [placeName]

  if len(result) == 0:
    print('You will never meet.')
  else:
    print(currentMin, end=" ")
    print(" ".join(result))


 # 2 graphs
 # 1 for young
 # 1 for aged
 # We dont know how many places
while True:
  m = int(input())

  if m == 0:
    break

  solve(m)
