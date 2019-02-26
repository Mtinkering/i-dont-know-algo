def createNode(x):
  newNode = Node()
  newNode.key = x

  return newNode


class Node:
  def __init__(self):
    self.key = 0
    self.left = None
    self.right = None


def insertNode(root, x):
  # Complexity is the height of tree
  #  trả về gốc của cây mới
  if root == None:
    return createNode(x)

  if x < root.key:
    root.left = insertNode(root.left, x)
  elif x > root.key:
    root.right = insertNode(root.right, x)

  # Tuỳ. tạm thời ko care duplicates
  return root


def createTree(a, n):
  root = None

  for i in range(n):
    root = insertNode(root, a[i])

  return root


def searchNode(root, x):
  if root == None or root.key == x:
    return root

  if root.key < x:
    return searchNode(root.right, x)

  return searchNode(root.left, x)


# - Only care about the root

# C++/ Java: Set: red-black tree in C++
# Python: use hash
