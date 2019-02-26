import queue


class Node:
  def __init__(self, id, dist):
    self.dist = dist
    self.id = id

  def __lt__(self, other):
    return self.dist <= other.dist


def dijkstra(graph, s, distance):
  # Queue contains items whose id is vertex and dist is the shortest distance from the source
  pq = queue.PriorityQueue()
  pq.put(Node(s, 0))
  distance[s] = 0

  while not pq.empty():
    top = pq.get()

    u = top.id
    weight = top.dist

    for neighbor in graph[u]:
      # source -> this,  + this -> neighbor < distance from the source to the neighbor
      if weight + neighbor.dist < distance[neighbor.id]:
        # This is the new shortest path
        distance[neighbor.id] = weight + neighbor.dist
        pq.put(Node(neighbor.id, distance[neighbor.id]))


n = int(input())
graph = [[] for i in range(501)]
distance = [float('inf') for i in range(501)]

for i in range(n):
  a, b, w = list(map(int, input().split()))

  graph[a].append(Node(b, w))
  graph[b].append(Node(a, w))


u = int(input())
dijkstra(graph, u, distance)

q = int(input())
for i in range(q):
  d = distance[int(input())]
  if d == float('inf'):
    print("NO PATH")
  else:
    print(d)
