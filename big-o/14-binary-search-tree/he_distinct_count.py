class Node:
  def __init__(self, x):
    self.key = x
    self.left = None
    self.right = None


def insertNode(root, num):
  if root == None:
    return Node(num)

  if num < root.key:
    root.left = insertNode(root.left, num)
  elif num > root.key:
    root.right = insertNode(root.right, num)

  return root

# Create tree with distinct elements


def createTree(arr):
  root = None

  for num in arr:
    root = insertNode(root, num)

  return root


def size(root):
  if root == None:
    return 0

  return size(root.left) + 1 + size(root.right)


def solve():
  n, x = map(int, input().split())

  arr = list(map(int, input().split()))

  # root = createTree(arr)
  root = set(arr)
  s = len(root)
  # s = size(root)

  if s == x:
    print("Good")
  elif s > x:
    print("Average")
  else:
    print("Bad")


t = int(input())

for _ in range(t):
  solve()
