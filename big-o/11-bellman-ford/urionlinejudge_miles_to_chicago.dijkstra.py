import queue


def dijkstra(s, graph, percentage):

  pq = queue.PriorityQueue()
  pq.put((1, s))
  percentage[s] = 1

  while not pq.empty():
    percent, id = pq.get()
    percent = -percent

    # if percent != percentage[id]:
    #   continue

    for neighbor in graph[id]:
      neighborId = neighbor[1]
      weight = neighbor[0]
      if percentage[id]*weight > percentage[neighborId]:
        percentage[neighborId] = percentage[id]*weight
        pq.put((percentage[neighborId], neighborId))


def solve(n, m):
  graph = [[] for i in range(n)]

  for _ in range(m):
    a, b, p = map(int, input().split())

    a -= 1
    b -= 1

    graph[a].append((p/100, b))
    graph[b].append((p/100, a))

  percentage = [0 for i in range(n)]
  dijkstra(0, graph, percentage)

  print("{0:.6f}".format(percentage[n-1]*100) + " percent")


data = input().split()

while len(data) != 1:
  solve(int(data[0]), int(data[1]))
  data = input().split()
