# import sys
# sys.setrecursionlimit(10**6)


class UnionFind:
  def __init__(self):
    self.size = {}
    self.parent = {}

  def union(self, u, v):
    if u not in self.size:
      self.size[u] = 1

    if v not in self.size:
      self.size[v] = 1

    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return

    if self.size[up] >= self.size[vp]:
      self.parent[vp] = up
      self.size[up] += self.size[vp]
    else:
      self.parent[up] = vp
      self.size[vp] += self.size[up]

  def find(self, u):
    if u not in self.parent:
      self.parent[u] = u

    if u == self.parent[u]:
      return self.parent[u]

    tmp = self.find(self.parent[u])
    self.parent[u] = tmp
    return tmp
#     if u != self.parent[u]:
#       self.parent[u] = self.find(u)

#     return self.parent[u]

  def findSize(self, u):
    return self.size[self.find(u)]


class Solution(object):
  def longestConsecutive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s = set(nums)
    uf = UnionFind()

    for num in nums:
      if num+1 in s:
        uf.union(num, num+1)
      else:
        uf.union(num, num)

    ans = 0
    for num in nums:
      if num == uf.find(num):
        ans = max(ans, uf.findSize(num))

    return ans


x = Solution()
print(x.longestConsecutive([100, 4, 200, 1, 3, 2]))
