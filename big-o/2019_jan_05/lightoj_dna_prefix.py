# http: // lightoj.com/volume_showproblem.php?problem = 1224


class Node():
  def __init__(self):
    self.child = {}
    self.countChild = 0


def addNode(root, word):
  tmp = root
  res = 0

  for i, c in enumerate(word):
    if c not in tmp.child:
      tmp.child[c] = Node()

    tmp = tmp.child[c]

    tmp.countChild += 1

    res = max(res, tmp.countChild*(i+1))

  return res


def solve():
  ans = 0

  n = int(input())

  trie = Node()

  for i in range(n):
    word = input()

    ans = max(ans, addNode(trie, word))

  return ans


t = int(input())

for i in range(t):
  res = solve()

  print('Case ' + str(i+1) + ': ' + str(res))

# Time complexity is O(len(s))
