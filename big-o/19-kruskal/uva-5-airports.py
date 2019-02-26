# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 2833
class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0 for i in range(n)]

  def union(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return

    if self.rank[up] == self.rank[vp]:
      self.parent[up] = vp
      self.rank[vp] += 1
    elif self.rank[up] < self.rank[vp]:
      self.parent[up] = vp
    else:
      self.parent[vp] = up

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]


def kruskal(edges, n, a):
  edges.sort(key=lambda x: x[2])

  uf = UnionFind(n)

  total = 0
  for edge in edges:
    u, v, w = edge

    if w >= a:
      continue

    up = uf.find(u)
    vp = uf.find(v)

    if up != vp:
      total += w
      uf.union(u, v)

  cluster = 0
  for i in range(n):
    if i == uf.find(i):
      cluster += 1

  return (total, cluster)


def solve(testNumber):
  n, m, a = map(int, input().split())

  roads = []
  for i in range(m):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    roads.append((x, y, c))

  (total, numberOfAirports) = kruskal(roads, n, a)
  cost = numberOfAirports*a + total

  print("Case #%d: %d %d" % (testNumber+1, cost, numberOfAirports))


def main():
  t = int(input())

  for testNumber in range(t):
    solve(testNumber)


main()
