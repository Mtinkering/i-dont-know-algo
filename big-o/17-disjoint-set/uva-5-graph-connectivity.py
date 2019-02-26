# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=400
# 30 minutes + no clue to move on: hint 1
# 15-20 minutes: hint 2:
# 15-20 minutes: hint 3


class UnionFind:
  def __init__(self, n):
    self.rank = [0 for i in range(n)]
    self.parent = [i for i in range(n)]

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

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
  t = int(input())

  input()

  for i in range(t):
    largest = input()
    n = ord(largest) - ord('A') + 1
    uf = UnionFind(n)

    pair = input()
    try:
      while pair != '':
        u = ord(pair[0]) - ord('A')
        v = ord(pair[1]) - ord('A')
        uf.union(u, v)
        pair = input()
    except Exception as e:
      # print(e)
      pass
    # TypeError: ord() expected a character, but string of length 2 found

    counter = 0
    for j in range(n):
      if j == uf.find(j):
        counter += 1
    print(counter)

    if i != t - 1:
      print()


main()
