# One node can contain a lot of information. utilize it
class Node:
  def __init__(self):
    self.countWord = 0  # End of word when countWord == 1. Số luong từ kết thúc ở vị trí này
    # self.countChild = 0
    # self.weight = max(self.weight, weight)  # Weight is some external value
    self.child = dict()

# Trie operation
# Add
# Search
# Delete
# Keys have to be an order of some kind
# Time Complexity O(string_length)
# Trùng: prefix
# Mỗi nút có thể có 26 nút con (nếu dùng ASCII)

# Search:
# 1. prefix
# 2. whole

# Delete
# 1. Delete words with some prefix
# 2. Delete one word


def addWord(root, s):
  tmp = root

  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]

  tmp.countWord += 1


def findWord(root, s):
  tmp = root

  for ch in s:
    if ch not in tmp.child:
      return False

    tmp = tmp.child[ch]

  return tmp.countWord > 0


def findPrefix(root, s):
  tmp = root

  for c in s:
    if c not in tmp.child:
      return False

    tmp = tmp.child[c]

  return True


def remove(root, word):
  return removeWord(root, word, 0)
# Return True if a word is deleted


def removeWord(root, s, level):
  if root == None:
    return False

  if level == len(s):
    if root.countWord > 0:
      root.countWord -= 1
      return True

    return False

  ch = s[level]

  res = removeWord(root.child[ch], s, level + 1)

  if res == True and len(root.child[ch].child) == 0 and root.child[ch].countWord == 0:
    del root.child[ch]

  return res


if __name__ == '__main__':
  root = Node()
  addWord(root, "the")
  addWord(root, "then")
  addWord(root, "then")
  addWord(root, "bigo")

  print(findPrefix(root, "t"))
  print(findWord(root, "there"))
  print(findWord(root, "th"))
  print(findWord(root, "the"))

  print(remove(root, "bigo"))
  print(remove(root, "the"))
  print(remove(root, "then"))

  print(len(root.child))


# python trick:
from collections import defaultdict


def _trie():
  return defaultdict(_trie)
