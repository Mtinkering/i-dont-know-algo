######################
## Attempted        ##
######################
# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1099
# Need to track identity of the enemy
# Time complexity:
# Space complexity:


class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n)]
    # self.rank = [1 for i in range(n)]
    self.enemy = [i for i in range(n)]

  def setFriends(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    # Same parent, return true as not contradict but do nothing
    if up == vp:
      return True

    ue = self.findE(up)
    # uep = -1
    # if ue != -1:
    #   uep = self.find(ue)

    ve = self.findE(vp)
    # vep = -1
    # if ve != -1:
    #   vep = self.find(ve)

    # Contradict because parent this a cluster is the enemy of another cluster
    if up == ve:
      return False

    # Otherwise union by rank
    # if self.rank[up] > self.rank[vp]:
    self.parent[vp] = up

    self.enemy[ue] = ve
    # self.enemy[up] = vp
    # if vep != -1 and uep != -1:
    # self.parent[vep] = uep

    # elif self.rank[up] == self.rank[vp]:
    #   self.rank[up] += 1
    #   self.parent[vp] = up

    # else:
    #   self.parent[up] = vp

    return True

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

  def findE(self, u):
    if u != self.enemy[u]:
      self.enemy[u] = self.findE(self.enemy[u])

    return self.enemy[u]

  def setEnemies(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return False

    ue = self.findE(up)
    ve = self.findE(vp)
    if ue == vp:
      return True

    # up = self.find(u)
    # ue = self.enemy[up]
    # uep = -1
    # if ue != -1:
    #   uep = self.find(ue)

    # vp = self.find(v)
    # ve = self.enemy[vp]
    # vep = -1
    # if ve != -1:
    #   vep = self.find(ve)

    # # Both don't have any enemy
    # if uep == -1 and vep == -1:
    #   self.enemy[up] = vp
    #   self.enemy[vp] = up
    # elif uep != -1 and vep == -1:
    #   self.setFriends(uep, v)
    # elif vep != -1 and uep == -1:
    #   self.setFriends(u, vep)
    # else:
    # self.setFriends(u, vep)
    # self.setFriends(v, uep)
    self.parent[]

    return True

  def areFriends(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    return up == vp

  def areEnemies(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    ue = self.findE(up)
    # if ue == -1:
    #   return False

    # uep = self.find(ue)

    return ue == vp


def main():
  n = int(input())
  uf = UnionFind(n)

  c, x, y = map(int, input().split())

  while c != 0 or x != 0 or y != 0:
    if c == 1:
      res = uf.setFriends(x, y)
      if res == False:
        print(-1)

    elif c == 2:
      res = uf.setEnemies(x, y)
      if res == False:
        print(-1)

    elif c == 3:
      res = uf.areFriends(x, y)

      print(1 if res else 0)
    else:
      res = uf.areEnemies(x, y)

      print(1 if res else 0)

    c, x, y = map(int, input().split())


main()


######################
## Solution         ##
######################
class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n*2)]
    self.size = n
    # self.rank = [1 for i in range(n)]
    # self.enemy = [-1 for i in range(n)]

  def setFriends(self, u, v):
    a1 = self.find(u)
    b1 = self.find(v)

    # Same parent, return true as not contradict but do nothing
    if a1 == b1:
      return True

    a2 = self.find(u+self.size)
    b2 = self.find(v+self.size)

    if a1 == b2:
      return False

    self.parent[a1] = b1
    self.parent[a2] = b2

    return True

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])

    return self.parent[u]

  def setEnemies(self, u, v):
    a1 = self.find(u)
    b1 = self.find(v)

    # Same parent, return true as not contradict but do nothing
    if a1 == b1:
      return False

    a2 = self.find(u+self.size)
    b2 = self.find(v+self.size)

    self.parent[a1] = b2
    self.parent[b1] = a2

    return True


def main():
  n = int(input())
  uf = UnionFind(n)

  c, x, y = map(int, input().split())

  while c != 0 or x != 0 or y != 0:
    if c == 1:
      res = uf.setFriends(x, y)
      if res == False:
        print(-1)

    elif c == 2:
      res = uf.setEnemies(x, y)
      if res == False:
        print(-1)

    elif c == 3:
      a1 = uf.find(x)
      b1 = uf.find(y)

      print(1 if a1 == b1 else 0)
    else:
      a1 = uf.find(x)
      b2 = uf.find(y+n)

      print(1 if a1 == b2 else 0)

    c, x, y = map(int, input().split())


main()


###########################
## Final Solution        ##
###########################

# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1099
# Need to track identity of the enemy
# Time complexity: not using rank so up to O(n + log(n)*f)
# Space complexity:


class UnionFind:
  def __init__(self, n):
    self.parent = [i for i in range(n*2)]
    self.offset = n

  def setFriends(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    # Same parent, return true as not contradict but do nothing
    if up == vp:
      return True

    ue = self.find(u + self.offset)
    ve = self.find(v + self.offset)

    if up == ve:
      return False

    self.parent[up] = vp
    self.parent[ue] = ve

    return True

  def setEnemies(self, u, v):
    up = self.find(u)
    vp = self.find(v)

    if up == vp:
      return False

    ue = self.find(u + self.offset)
    ve = self.find(v + self.offset)

    # Return early
    if up == ve:
      return True

    self.parent[up] = ve
    self.parent[vp] = ue

    return True

  def find(self, u):
    if u != self.parent[u]:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]


def main():
  n = int(input())
  uf = UnionFind(n)

  c, u, v = map(int, input().split())

  while c != 0 or u != 0 or v != 0:
    if c == 1:
      res = uf.setFriends(u, v)
      if res == False:
        print(-1)

    elif c == 2:
      res = uf.setEnemies(u, v)
      if res == False:
        print(-1)

    elif c == 3:
      up = uf.find(u)
      vp = uf.find(v)

      print(1 if up == vp else 0)
    else:
      up = uf.find(u)
      ve = uf.find(v+n)

      print(1 if up == ve else 0)

    c, u, v = map(int, input().split())


main()
