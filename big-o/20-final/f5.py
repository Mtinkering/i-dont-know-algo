class Node:
  def __init__(self):
    self.children = {}
    self.endOfWord = False


def addNode(root, s):
  cur = root
  endOfWord = False
  noNewChar = True
  for c in s:
    if c not in cur.children:
      cur.children[c] = Node()
      noNewChar = False

    cur = cur.children[c]
    if cur.endOfWord == True:
      endOfWord = True

  cur.endOfWord = True

  return endOfWord or noNewChar


def solve():
  n = int(input())
  trie = Node()
  res = 'YES'
  for _ in range(n):
    s = input()
    isPrefix = addNode(trie, s)
    if isPrefix:
      res = 'NO'

  print(res)


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
