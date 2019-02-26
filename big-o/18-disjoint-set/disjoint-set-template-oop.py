class UnionFind:
  def __init__(self, n):
    self.parents = list(range(n))
    self.rank = [0] * n

  def find(self, x):
    if self.parents[x] != x:
      self.parents[x] = self.find(self.parents[x])
    return self.parents[x]

  def union(self, x, y):
    rx = self.find(x)
    ry = self.find(y)

    if self.rank[rx] > self.rank[ry]:
      self.parents[ry] = rx
    elif self.rank[rx] < self.rank[ry]:
      self.parents[rx] = ry
    else:
      self.parents[rx] = ry
      self.rank[ry] += 1


class Solution:
  def findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """

    if not M or len(M) == 0:
      return 0

    N = len(M)
    uf = UnionFind(N)

    for i in range(0, N):
      for j in range(i+1, N):
        if M[i][j] == 1 and uf.find(i) != uf.find(j):
          uf.union(i, j)

    # clear path compression
    return len(set([uf.find(i) for i in uf.parents]))
