# https: // www.spoj.com/problems/LOSTNSURVIVED/
# Need a way to track min values. PriorityQueue is a good candidate
# Use heapq for performance
# Time Complexity is O(N + Q), because the findMinSize complexity is low if we do it often enough
# Space complexity is O(N)
import heapq


class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.size = [1 for i in range(n)]
    # self.minSize = queue.PriorityQueue()
    self.minSize = [(1, i) for i in range(n)]
    heapq.heapify(self.minSize)

    # for i in range(n):
    #   self.minSize.put((1, i)) # Store the size and the represent

  def union(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return

    if self.size[up] > self.size[vp]:
      self.parent[vp] = up
      self.size[up] += self.size[vp]

      # self.minSize.put((self.size[up], up))
      heapq.heappush(self.minSize, (self.size[up], up))
    else:
      self.parent[up] = vp
      self.size[vp] += self.size[up]

      # self.minSize.put((self.size[vp], vp))
      heapq.heappush(self.minSize, (self.size[vp], vp))

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

  def findSize(self, u):
    return self.size[self.find(u)]

  def findMinSize(self):
    size, u = self.minSize[0]

    if u != self.parent[u] or self.findSize(u) != size:
      heapq.heappop(self.minSize)
      return self.findMinSize()
    else:
      return size


def main():
  n, q = map(int, input().split())

  uf = UnionFind(n)
  maxSize = -1
  minSize = 10**6

  for _ in range(q):
    u, v = map(lambda x: int(x) - 1, input().split())

    uf.union(u, v)

    uSize = uf.findSize(u)

    if uSize > maxSize:
      maxSize = uSize

    minSize = uf.findMinSize()

    print(maxSize - minSize)


main()
