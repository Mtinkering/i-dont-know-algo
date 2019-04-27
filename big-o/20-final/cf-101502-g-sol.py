# https: // codeforces.com/gym/101502/problem/G
# Nen build memoiz when constructing the trie


class Node:
  def __init__(self):
    self.children = {}
    self.count = 0


def addString(root, s, memoiz):
  cur = root
  level = 1
  for i in range(len(s)-1, -1, -1):
    c = s[i]
    if c not in cur.children:
      cur.children[c] = Node()

    cur = cur.children[c]
    cur.count += 1

    if level not in memoiz:
      memoiz[level] = 0
    memoiz[level] = max(memoiz[level], cur.count)
    level += 1


# def retrieveFrequency(root, currentLevel, level, memoiz):
#   # print(root, level, memoiz)
#   cur = root
#   ans = 0

#   if currentLevel == level:
#     for c in cur.children.keys():
#       ans = max(ans, cur.children[c].count)
#     # return ans
#   else:
#     for c in cur.children.keys():
#       ans = max(retrieveFrequency(cur.children[c], level-1, memoiz), ans)

#   memoiz[level] = ans
#   # print(memoiz)
#   return ans

# O(q + m)


def solve():
  n, q = map(int, input().split())
  root = Node()
  memoiz = {}
  for _ in range(n):
    addString(root, input(), memoiz)

    # print(memoiz)
  for _ in range(q):
    x = int(input())
    # if x not in memoiz:
    # retrieveFrequency(root, 0, x, memoiz)

    print(memoiz[x])


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
