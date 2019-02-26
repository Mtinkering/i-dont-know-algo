# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 3676
def distance(a, b):
  total = 0
  for i in range(4):
    delta = abs(int(a[i]) - int(b[i]))
    if delta > 5:
      delta = 10 - delta

    total += delta
  return total


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


def kruskal(edges, k):
  edges.sort(key=lambda edge: edge[2])

  uf = UnionFind(k)

  total = 0
  counter = 0
  for edge in edges:
    u, v, _ = edge
    # up = uf.find(u)
    # vp = uf.find(v)

    hasUnioned = uf.union(u, v)
    if hasUnioned == True:
      total += edge[2]
      # uf.union(u, v)
      counter += 1

      if counter == k - 1:
        return total

  return -1


def solve():
  data = input().split()
  n = int(data[0])

  edges = []
  for i in range(n):
    for j in range(i+1, n):
      d = distance(data[i+1], data[j+1])
      edges.append((i, j, d))

  mst = kruskal(edges, n)

  m = 10**9
  for i in range(n):
    d = distance(data[i+1], '0000')
    m = min(m, d)

  print(mst+m)


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
