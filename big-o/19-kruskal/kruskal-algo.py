class Triad:
  def __init__(self, source, target, weight):
    self.source = source
    self.target = target
    self.weight = weight


parent = []
ranks = []
dist = []
graph = []


def makeSet(V):
  global parent, ranks
  parent = [i for i in range(V+1)]
  ranks = [0 for i in range(V+1)]


def findSet(u):
  if parent[u] != u:
    parent[u] = findSet(parent[u])

  return parent[u]


def unionSet(u, v):
  up = findSet(u)
  vp = findSet(u)

  if up == vp:
    return

  if ranks[up] == ranks[vp]:
    parent[up] = vp
    ranks[vp] += 1
  elif ranks[up] < ranks[vp]:
    parent[up] = vp
  else:
    parent[vp] = up


def printMST():
  ans = 0
  for e in dist:
    print("%d - %d: %d" % (e.source, e.target, e.weight))
    ans += e.weight
  print("Total weight: %d" % ans)


def Kruskal(V):
  graph.sort(key=lambda edge: edge.weight)
  i = 0
  while len(dist) != V - 1:
    edge = graph[i]
    i += 1
    u = findSet(edge.source)
    v = findSet(edge.target)

    if u != v:
      dist.append(edge)
      unionSet(u, v)


if __name__ == '__main__':
  V, E = map(int, input().split())

  for i in range(E):
    u, v, w = map(int, input().split())
    graph.append(Triad(u, v, w))

  makeSet(V)
  Kruskal(V)
  printMST()
