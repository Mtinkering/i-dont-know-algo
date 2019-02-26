
#  1 - 4 - 6 - 3
#  | .|
#  5 -|
#  |
#  2


#  n vertices
#  n - 1 edges + 1 = n edges

# The importance is to need one more edge
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


O(m+n)
Space: O(V+E)


def main():

  n, m = map(int, input().split())

  if m != n:
    print('NO')
    return

  uf = UnionFind(n)

  for i in range(m):  # m times
    u, v = map(lambda x: int(x) - 1, input().split())
    uf.union(u, v)

  counter = 0
  for i in range(n):
    if i == uf.find(i):
      counter += 1

  print('FHTAGN!' if counter == 1 else 'NO')


main()
