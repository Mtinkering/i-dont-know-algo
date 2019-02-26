# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & category = &problem = 2957
# ElogV


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


def kruskal(edges, n):
  edges.sort(key=lambda x: x[2])

  uf = UnionFind(n)

  numberOfUnion = 0
  minRange = -1
  for edge in edges:
    u, v, w = edge

    up = uf.find(u)
    vp = uf.find(v)

    if up != vp:
      uf.union(u, v)
      numberOfUnion += 1
      minRange = w

  if numberOfUnion < n - 1:
    return -1

  return minRange


def solve(n, m):
  roads = []
  for _ in range(m):
    c1, c2, l = map(int, input().split())
    roads.append((c1, c2, l))

  mst = kruskal(roads, n)

  print(mst if mst != -1 else "IMPOSSIBLE")


def main():
  n, m = map(int, input().split())

  while n != 0 or m != 0:
    solve(n, m)
    n, m = map(int, input().split())


main()
