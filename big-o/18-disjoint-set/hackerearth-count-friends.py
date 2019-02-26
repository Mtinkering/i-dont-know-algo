# https: // www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/count-friends/
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
      self.size[up] = self.size[up] + self.size[vp]
    else:
      self.parent[up] = vp
      self.size[vp] = self.size[vp] + self.size[up]

  def find(self, u):
    if self.parent[u] == u:
      return u

    self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

  def findSize(self, u):
    return self.size[self.find(u)]


def main():
  n, m = map(int, input().split())

  union = UnionFind(n)

  for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())

    union.union(u, v)

  ans = []
  for i in range(n):
    s = union.findSize(i)
    ans.append(s - 1)

  print(*ans)


main()
