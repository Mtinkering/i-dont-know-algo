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
