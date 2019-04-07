MOD = 10**9+7


class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0]*n

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
  k = 0
  ans = 1
  for u, v, w in edges:
    up = uf.find(u)
    vp = uf.find(v)

    if up != vp:
      uf.union(up, vp)

      k += 1
      ans = (ans*w) % MOD

    if k == n - 1:
      return ans

  return -1


def solve():
  n, m = map(int, input().split())

  edges = []
  for _ in range(m):
    a, b, c = map(int, input().split())

    edges.append((a-1, b-1, c))

  mst = kruskal(edges, n)
  print(mst)


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
