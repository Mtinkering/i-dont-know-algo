# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 2678
class UnionFind:
  def __init__(self, m):
    self.parent = [i for i in range(m)]
    self.rank = [0 for i in range(m)]

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]

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


def kruskal(edges, m):
  edges.sort(key=lambda x: x[2])
  uf = UnionFind(m)

  total = 0
  counter = 0
  i = 0
  while counter != m - 1:
    u, v, w = edges[i]

    up = uf.find(u)
    vp = uf.find(v)
    if up != vp:
      counter += 1
      total += w
      uf.union(up, vp)

    i += 1

  return total


def solve(m, n):
  edges = []
  total = 0
  for _ in range(n):
    x, y, z = map(int, input().split())
    edges.append((x, y, z))
    total += z
  print(total - kruskal(edges, m))


def main():
  m, n = map(int, input().split())

  while n != 0 or m != 0:
    solve(m, n)
    m, n = map(int, input().split())


main()
