# https: // codeforces.com/gym/101502/problem/G


class Node:
  def __init__(self):
    self.children = {}
    self.count = 0


def addString(root, s):
  cur = root

  for i in range(len(s)-1, -1, -1):
    c = s[i]
    if c not in cur.children:
      cur.children[c] = Node()

    cur = cur.children[c]
    cur.count += 1


def retrieveFrequency(root, level):
  cur = root
  ans = 0

  if level == 1:
    for c in cur.children.keys():
      ans = max(ans, cur.children[c].count)

    return ans

  for c in cur.children.keys():
    ans = max(retrieveFrequency(cur.children[c], level-1), ans)
  return ans


def solve():
  n, q = map(int, input().split())
  root = Node()

  for _ in range(n):
    addString(root, input())
  for _ in range(q):
    x = int(input())
    ans = retrieveFrequency(root, x)
    print(ans)


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
