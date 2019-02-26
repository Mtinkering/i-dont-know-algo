# https: // codeforces.com/problemset/problem/217/A
# 30 minutes + no clue to move on: hint 1
# 15-20 minutes: hint 2:
# 15-20 minutes: hint 3


class UnionFind:
  def __init__(self, points):
    self.rank = [0 for i in range(len(points))]
    self.parent = [i for i in range(len(points))]
    self.points = points

  def find(self, u):
    if self.points[u] != self.points[self.parent[u]]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

  def findCoordinate(self, u):
    return self.points[self.find(u)]

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

# Main logic


def main():
  n = int(input())

  coords = []
  for i in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

  uf = UnionFind(coords)

  for i in range(n):
    for j in range(n):
      if i != j:
        if coords[i][0] == coords[j][0] or coords[i][1] == coords[j][1]:
          uf.union(i, j)

  counter = 0
  for i in range(n):
    if coords[i] == uf.find(i):
      counter += 1

  print(counter - 1)


main()
