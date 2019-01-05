# https: // www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/search-engine/


class Node():
  def __init__(self):
    self.child = {}
    self.weight = 0


def addNode(root, word, weight):
  tmp = root

  for c in word:
    if c not in tmp.child:
      tmp.child[c] = Node()

    tmp = tmp.child[c]
    tmp.weight = max(tmp.weight, weight)


def findWord(root, word):
  tmp = root

  for c in word:
    if c not in tmp.child:
      return -1

    tmp = tmp.child[c]

  return tmp.weight


n, q = map(int, input().split())

trie = Node()

for i in range(n):
  word, weight = input().split()

  addNode(trie, word, int(weight))

for i in range(q):
  word = input()

  res = findWord(trie, word)

  print(res)
