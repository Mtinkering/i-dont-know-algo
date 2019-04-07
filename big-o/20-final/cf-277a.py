class UnionFind:
  def __init__(self, n, m):
    self.data = [i for i in range(n+m)]
    self.size = [0]*(m+n)

  def union(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return

    if self.size[up] <= self.size[vp]:
      self.data[up] = vp
      self.size[vp] += self.size[up]
    else:
      self.data[vp] = up
      self.size[up] += self.size[vp]

  def find(self, v):
    if v != self.data[v]:
      self.data[v] = self.find(self.data[v])

    return self.data[v]


def main():
  n, m = map(int, input().split())

  uf = UnionFind(n, m)
  anyLanguageLearned = False

  for i in range(n):
    data = input().split()
    k = int(data[0])

    for j in range(1, k+1):
      language = int(data[j]) - 1 + n
      uf.union(i, language)
      anyLanguageLearned = True

  # languages = set()
  cnt = 0
  for i in range(n+m):
    # language = uf.find(i)
    if i == uf.find(i):
      cnt += 1
    # languages.add(language)

  if anyLanguageLearned:
    # print(len(languages) - 1)
    print(cnt - 1)
  else:
    print(n)


main()
# Special case
# 2 2
# 0
# 0

# time: O(n*m)
# space: O(n+m)
