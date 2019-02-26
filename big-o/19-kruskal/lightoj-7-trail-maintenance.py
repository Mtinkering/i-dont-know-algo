# http: // lightoj.com/volume_showproblem.php?problem = 1123
import queue


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


def solve(t):
  print("Case %d:", (t+1))

  n, w = map(int, input().split())
  uf = UnionFind(n)

  numberOfUnion = 0

  edges = queue.PriorityQueue()
  # w - 1 edge: minimum spanning tree
  # then find the new one?
  #
  total = 0
  for i in range(w):
    u, v, l = map(int, input().split())
    u -= 1
    v -= 1
    up = uf.find(u)
    vp = uf.find(v)

    if up != vp:
      uf.union(u, v)
      numberOfUnion += 1
      total += l
      edges.put(-l)
    else:
      edges.put(-l)
      last = edges.get()

      total = total + l - (-last)

    # print(edges.queue, total, numberOfUnion)
    if numberOfUnion < n - 1:
      print(-1)
    else:
      print(total)


def main():
  t = int(input())

  for test in range(t):
    solve(test)


main()
