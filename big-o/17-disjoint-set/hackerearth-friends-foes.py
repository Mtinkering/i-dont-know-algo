# https: // www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/friends-and-foes/description/
# Time complexity O(m1 + m2 + N)
# Space O(N)


class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.size = [1 for i in range(n)]
    self.check = [True for i in range(n)]

  def unionFriend(self, u, v):
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

  def unionEnemy(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      self.check[up] = False

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

  def findValidGroup(self, u):
    up = self.find(u)

    if self.check[up] == True:
      return self.size[up]
    else:
      return 0


def main():
  n = int(input())
  uf = UnionFind(n)

  m1 = int(input())
  for _ in range(m1):
    u, v = map(lambda x: int(x) - 1, input().split())
    uf.unionFriend(u, v)

  m2 = int(input())
  for _ in range(m2):
    u, v = map(lambda x: int(x) - 1, input().split())
    uf.unionEnemy(u, v)

  maxSize = -1
  for i in range(n):
    size = uf.findValidGroup(i)

    maxSize = max(size, maxSize)

  print(maxSize)


main()
