# https: // uva.onlinejudge.org/index.php?option = onlinejudge & page = show_problem & problem = 1756
import re


def strFilter(string):
  return re.sub(r"[^A-Za-z]+", ' ', string).lower()


# Add then sort
# O(line*characters + distinct*log(distinct)*comparison cost)
# wordSet = set()
# while True:
#   try:
#     line = input()

#     words = map(strFilter, line.strip().split())

#     for word in words:
#       if len(word) > 0:
#         wordSet.add(word)

#   except Exception:
#     break

# for word in wordSet:
#   print(word)


# Binary Search tree


class Node:
  def __init__(self, w):
    self.key = w
    self.left = None
    self.right = None


def insertNode(root, word):
  if root == None:
    return Node(word)
  if word < root.key:
    root.left = insertNode(root.left, word)
  elif word > root.key:
    root.right = insertNode(root.right, word)
  return root


root = None

while True:
  try:
    line = input()

    newLine = strFilter(line)
    words = newLine.split()

    for word in words:
      if len(word) > 0:
        root = insertNode(root, word)

  except Exception:
    break


def treeTraversal(root):
  if root == None:
    return

  treeTraversal(root.left)

  print(root.key)

  treeTraversal(root.right)


treeTraversal(root)
