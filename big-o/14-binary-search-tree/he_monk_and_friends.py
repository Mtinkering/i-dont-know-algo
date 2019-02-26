class Node:
  def __init__(self, x):
    self.key = x
    self.left = None
    self.right = None


def insertNode(root, x):
  if root == None:
    return Node(x)

  if x < root.key:
    root.left = insertNode(root.left, x)
  elif x > root.key:
    root.right = insertNode(root.right, x)

  return root


def createTree(arr, n):
  root = None

  for i in range(n):
    root = insertNode(root, arr[i])

  return root


def searchNode(root, x):
  if root == None or root.key == x:
    return root

  if x < root.key:
    return searchNode(root.left, x)

  return searchNode(root.right, x)


for _ in range(int(input())):
  n, m = map(int, input().split())

  students = list(map(int, input().split()))

  root = createTree(students, n)

  for i in range(m):
    x = students[n+i]
    res = searchNode(root, x)

    if res != None:
      print('YES')
    else:
      print('NO')

    insertNode(root, x)
