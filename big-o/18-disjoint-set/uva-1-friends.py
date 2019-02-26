# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 1549
class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.size = [1 for i in range(n)]

  def union(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return

    if self.size[up] > self.size[vp]:
      self.parent[vp] = up
      self.size[up] += self.size[vp]
    else:
      self.parent[up] = vp
      self.size[vp] += self.size[up]

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

  def findSize(self, u):
    return self.size[self.find(u)]


# O(N*alpha(n))

def main():
  t = int(input())

  for i in range(t):
    n, m = map(int, input().split())

    uf = UnionFind(n)

    for i in range(m):
      u, v = map(lambda x: int(x) - 1, input().split())

      uf.union(u, v)

    ans = -1
    for i in range(n):
      ans = max(ans, uf.findSize(i))

    print(ans)


main()
