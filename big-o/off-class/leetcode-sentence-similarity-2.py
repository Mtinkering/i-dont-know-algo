# https: // leetcode.com/problems/sentence-similarity-ii/
# Solve with union by rank, to make every operation ~ O(1)


class UnionFind:
  def __init__(self):
    self.parent = {}
    self.rank = {}

  def union(self, u, v):
    if u not in self.parent:
      self.parent[u] = u

    if v not in self.parent:
      self.parent[v] = v

    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return

    if up not in self.rank:
      self.rank[up] = 0

    if vp not in self.rank:
      self.rank[vp] = 0

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

  def check(self, u, v):
    if u not in self.parent or v not in self.parent:
      return False

    up = self.find(u)
    vp = self.find(v)
    return up == vp


class Solution:
  def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
    if len(words1) != len(words2):
      return False

    uf = UnionFind()
    for u, v in pairs:
      uf.union(u, v)

    for i in range(len(words1)):
      s1 = words1[i]
      s2 = words2[i]

      if s1 == s2:
        continue

      if uf.check(s1, s2) == False:
        return False

    return True
