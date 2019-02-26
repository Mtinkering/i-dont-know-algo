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

# Complexity is the number of operation because each operation is optimized with path compression and union by rank
