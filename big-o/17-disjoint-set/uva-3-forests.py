# https: // uva.onlinejudge.org/external/102/10227.pdf
# Time complexity: O(p*tlogt)
# Space complexity: O(p*t)

test = int(input())

input()
for _ in range(test):

  p, t = map(int, input().split())

  persons = [set() for i in range(p)]

  data = input()
  ans = 0
  try:
    while data != "":
      i, j = map(int, data.split())
      i -= 1
      persons[i].add(j)

      data = input()

  except:
    pass

  for i in range(p):
    l = list(persons[i])
    l.sort()
    persons[i] = tuple(l)

  print(len(set(persons)))

  if _ != test - 1:
    print()


######################
## DSU              ##
######################
# https: // uva.onlinejudge.org/external/102/10227.pdf
# Time complexity: O(p**3)
# Space complexity: O(p**2)


class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [0 for i in range(n)]

  def union(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return

    if self.rank[up] > self.rank[vp]:
      self.parent[vp] = up
    elif self.rank[up] < self.rank[vp]:
      self.parent[up] = vp
    else:
      self.parent[up] = vp
      self.rank[vp] += 1

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]


test = int(input())

input()
for _ in range(test):

  p, t = map(int, input().split())

  uf = UnionFind(p)

  persons = [set() for i in range(p)]

  data = input()
  ans = 0
  try:
    while data != "":
      i, j = map(int, data.split())
      i -= 1
      persons[i].add(j)

      data = input()

  except:
    pass

  for i in range(p):
    for j in range(i+1, p):
      if persons[i] == persons[j]:
        uf.union(i, j)

  ans = set()
  for i in range(p):
    ans.add(uf.find(i))
  print(len(ans))

  if _ != test - 1:
    print()
