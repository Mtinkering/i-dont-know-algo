# https: // icpcarchive.ecs.baylor.edu/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 3803
def solve(p, s):
  portu = []
  nol = []

  for i in range(p):
    portu.append(input())

  for i in range(s):
    nol.append(input())

  counter = 0
  words = set()

  for pword in portu:
    for k in range(1, len(pword)+1):
      psub = pword[:k]

      for sword in nol:
        for l in range(0, len(sword)):
          ssub = sword[l:]

          newWord = psub + ssub

          if newWord not in words:
            counter += 1
            words.add(newWord)

  print(counter)


def main():
  p, s = map(int, input().split())

  while p != 0 or s != 0:
    solve(p, s)
    p, s = map(int, input().split())


main()


##################
# version 2        #
##################

# https: // icpcarchive.ecs.baylor.edu/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 3803


class Node:
  def __init__(self):
    self.child = {}
    self.end = False


def addNode(root, w):
  cur = root
  added = False
  for c in w:
    if c not in cur.child:
      cur.child[c] = Node()
      added = True
    cur = cur.child[c]
  cur.end = True

  return added


def addNewNode(root, w):
  print("word = " + w)
  cur = root
  counter = 0
  queue = [root]

  while len(queue) != 0:
    temp = []
    for cur in queue:
      for child in cur.child:
        node = cur.child[child]
        temp.append(node)
        res = addNode(node, w)
        if res == True:
          counter += 1
    print(temp)
    queue = temp

  return counter


def solve(p, s):
  prefix = Node()
  for _ in range(p):
    w = input()

    addNode(root, w[:k])

  counter = 0
  for _ in range(s):
    w = input()

    for l in range(0, len(w)):
      counter += addNewNode(root, w[l:])

  print(counter)


def main():
  p, s = map(int, input().split())

  while p != 0 or s != 0:
    solve(p, s)
    p, s = map(int, input().split())


main()


##################
# Version 3        #
##################

# abc

# dbabc
# edabc

# a -> b -> c -> r -> d
# c -> b -> a


# ab .  c
# a .   bc

# abcr . c
# abc . bc


# {
#   b:
# }

# root ->  d -> b -> a -> b -> c
# root ->  e -> d -> a -> b -> c

# ab
# a bc, ab c
# # a bd, ab d
# a babc
# ab abc


# a
# a: - add only 1 more character -> ac
#    - add string longer than 1 -> avoid using suffices
#                           start with b: a abc,

# ab: - ab c
#     - ab bc, ab abc

# abc: - abc c
#      - abc bc, abc abc


# abc . * abc . = 9 - 1

# def dfs(root, freqS):

#   st = [root.child[c] for c in root.child]
#   counter = 0

#   while len(st) != 0:
#     node = st.pop()

#     for c in node.child:
#       if c in freqS and freqS[c] > 0:
#         freqS[c] -= 1
#       else:
#         counter += 1

#       st.append(node.child[c])

#   return counter


def dfs(root):

  st = [root]
  counter = 0

  while len(st) != 0:
    node = st.pop()

    for c in node.child:
      st.append(node.child[c])

      counter += 1

  return counter


class Node:
  def __init__(self):
    self.child = {}


def addNode(root, w, freqP):
  cur = root
  level = 0
  for c in w:
    if c not in cur.child:
      cur.child[c] = Node()
    cur = cur.child[c]

    if level > 0:
      freqP[c] = freqP.get(c, 0) + 1

    level += 1


def solve(p, s):
  prefix = Node()
  suffix = Node()
  x = 0
  y = 0

  freqP = {}
  for _ in range(p):
    w = input()
    addNode(prefix, w, freqP)

  freqS = {}
  for _ in range(s):
    w = input()

    addNode(suffix, reversed(w), freqS)

  # print(freqP)
  # print(freqS)

  x = dfs(prefix)
  y = dfs(suffix)
  # print(x, y)
  counter = 0
  for k, v in freqP.items():
    if k in freqS:
      counter += v*freqS[k]
  # counter = dfs(prefix, freqS)

  print(x*y - counter)


def main():
  p, s = map(int, input().split())

  while p != 0 or s != 0:
    solve(p, s)
    p, s = map(int, input().split())


main()
