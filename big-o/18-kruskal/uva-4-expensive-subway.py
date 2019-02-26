# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 2757
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

# 1
# 2-3
# 3-4
# 2-4

# 1-2

# 3-4
# 4-5
# # 3-5
# start from 3
# dist[u] != INF


def kruskal(edges, n, src):
  edges.sort(key=lambda x: x[2])

  uf = UnionFind(n)

  total = 0
  numberOfUnion = 0
  for edge in edges:
    u, v, w = edge
    up = uf.find(u)
    vp = uf.find(v)

    if up != vp:
      total += w
      uf.union(u, v)
      numberOfUnion += 1

  # sp = uf.find(src)
  # for i in range(n):
  #   ip = uf.find(i)
  #   if ip != sp:
  #     return -1

  return total if numberOfUnion == n - 1 else -1


def solve(s, c):
  nameToIndex = {}

  for i in range(s):
    name = input()
    nameToIndex[name] = i

  connections = []
  for i in range(c):
    s1, s2, cost = input().split()
    connections.append((nameToIndex[s1], nameToIndex[s2], int(cost)))

  src = input()

  mst = kruskal(connections, s, nameToIndex[src])

  print("Impossible" if mst == -1 else mst)


def main():
  s, c = map(int, input().split())

  while s != 0 or c != 0:
    solve(s, c)
    s, c = map(int, input().split())


main()
