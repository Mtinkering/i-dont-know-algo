# import sys
# sys.setrecursionlimit = 10000


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

  def find(self, v):
    if self.parent[v] != v:
      self.parent[v] = self.find(self.parent[v])

    return self.parent[v]


def solve(n, m, t):
  ans = 0
  uf = UnionFind(n)

  for i in range(m):
    u, v = map(int, input().split())
    uf.union(u-1, v-1)

  for i in range(n):
    if i == uf.find(i):
      ans += 1

  print("Case " + str(t) + ": " + str(ans))


def main():
  t = 1

  n, m = map(int, input().split())
  while m != 0 or n != 0:
    solve(n, m, t)
    n, m = map(int, input().split())
    t += 1


main()
