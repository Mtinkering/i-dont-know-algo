# https: // uva.onlinejudge.org/index.php?option = onlinejudge & page = show_problem & problem = 1756
import re


def strFilter(string):
  return re.sub(r"[^A-Za-z-]+", ' ', string).lower()


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
lastWord = ''
while True:
  try:
    line = input()

    newLine = strFilter(line)
    words = newLine.split()

    for i, word in enumerate(words):
      if len(word) > 0:
        # First word
        if i == 0 and lastWord != '':
          word = lastWord[:len(lastWord)-1] + word
          lastWord = ''

        # Last word
        if i == len(words) - 1 and word[-1] == '-':
          lastWord = word
        else:
          root = insertNode(root, word)

  except Exception:
    # Last one
    if lastWord != '':
      root = insertNode(root, word)
    break


def treeTraversal(root):
  if root == None:
    return

  treeTraversal(root.left)

  print(root.key)

  treeTraversal(root.right)


treeTraversal(root)
