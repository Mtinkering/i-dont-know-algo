class UnionFind:
  def __init__(self, x, y):
    self.parent = [i for i in range(x + y)]
    self.nwomen = [0] * x + [1]*y
    self.size = [1] * (x+y)

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])

    return self.parent[x]

  def union(self, x, y):
    xp = self.find(x)
    yp = self.find(y)

    if xp == yp:
      return

    if self.size[xp] > self.size[yp]:
      self.parent[yp] = xp
      self.size[xp] += self.size[yp]
      self.nwomen[xp] += self.nwomen[yp]
    else:
      self.parent[xp] = yp
      self.size[yp] += self.size[xp]
      self.nwomen[yp] += self.nwomen[xp]

  def numberOfWomen(self, i):
    return self.nwomen[self.find(i)]


def main():
  x, y = map(int, input().split())

  uf = UnionFind(x, y)

  for i in range(int(input())):
    u, v = map(lambda k: int(k) - 1, input().split())
    uf.union(u, v)

  for i in range(int(input())):
    u, v = map(lambda k: int(k) - 1 + x, input().split())
    uf.union(u, v)

  for i in range(int(input())):
    u, v = map(int, input().split())
    u -= 1
    v = v - 1 + x
    uf.union(u, v)

  p = 0
  for i in range(x):
    p += (y - uf.numberOfWomen(i))

  print(p)


main()
