# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 3649
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


def kruskal(edges, n):
  edges.sort(key=lambda edge: edge[2])
  uf = UnionFind(n)

  ans = []
  counter = 0
  for edge in edges:
    u, v, _ = edge

    hasUnioned = uf.union(u, v)
    if hasUnioned == True:
      ans.append(edge)
      counter += 1

      if counter == n - 1:
        return ans

  return []


def toCity(u):
  return chr(ord('A') + u)


def solve(testNumber):
  n = int(input())
  edges = []
  for i in range(n):
    data = list(map(int, input().split(', ')))
    for j in range(n):
      if data[j] != 0:
        edges.append((i, j, data[j]))

  ans = kruskal(edges, n)
  print("Case %d:" % (testNumber+1))
  for edge in ans:
    u, v, w = edge

    print("%s-%s %d" % (toCity(u), toCity(v), w))


def main():
  t = int(input())

  for i in range(t):
    solve(i)


main()
