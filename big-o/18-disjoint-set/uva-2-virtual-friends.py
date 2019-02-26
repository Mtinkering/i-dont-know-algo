# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 2498
# from collections import defaultdict


class UnionFind:
  def __init__(self):
    self.parent = {}
    self.size = {}

  def union(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up not in self.size:
      self.size[up] = 1

    if vp not in self.size:
      self.size[vp] = 1

    if up == vp:
      return

    if self.size[up] > self.size[vp]:
      self.parent[vp] = up
      self.size[up] += self.size[vp]
    else:
      self.parent[up] = vp
      self.size[vp] += self.size[up]

  def find(self, u):
    if u not in self.parent:
      self.parent[u] = u

    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

  def findSize(self, u):
    return self.size[self.find(u)]


def main():
  t = int(input())

  for _ in range(t):

    uf = UnionFind()

    f = int(input())

    for _ in range(f):
      u, v = input().split()

      uf.union(u, v)
      print(uf.findSize(u))


main()
