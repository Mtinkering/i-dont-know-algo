def distance(c1, c2):
  x1, y1 = c1
  x2, y2 = c2
  return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0 for i in range(n)]

  def union(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return False

    if self.rank[up] == self.rank[vp]:
      self.parent[up] = vp
      self.rank[vp] += 1
    elif self.rank[up] < self.rank[vp]:
      self.parent[up] = vp
    else:
      self.parent[vp] = up

    return True

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]


def kruskal(n, edges):
  edges.sort(key=lambda edge: edge[2])
  k = 0
  i = 0
  total = 0
  uf = UnionFind(n)

  while k != n - 1:
    edge = edges[i]
    i += 1
    u = uf.find(edge[0])
    v = uf.find(edge[1])

    if u != v:
      k += 1
      uf.union(u, v)
      total += edge[2]

  return total


def solve():
  n = int(input())

  coords = []
  for i in range(n):
    x, y = map(float, input().split())
    coords.append((x, y))

  edges = []
  for i in range(n):
    for j in range(i+1, n):
      d = distance(coords[i], coords[j])
      edges.append((i, j, d))

  mst = kruskal(n, edges)
  print("%.2f" % mst)


def main():
  t = int(input())
  for i in range(t):
    input()
    solve()
    if i != t - 1:
      print()


main()
