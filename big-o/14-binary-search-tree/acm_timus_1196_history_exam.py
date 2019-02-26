class Node:
  def __init__(self, tup):
    self.key = tup
    self.left = None
    self.right = None


def insertNode(root, x):
  if root == None:
    return Node(x)

  if x[0] < root.key[0]:
    root.left = insertNode(root.left, x)
  elif x[0] > root.key[0]:
    root.right = insertNode(root.right, x)
  else:
    root.key = (root.key[0], root.key[1] + 1)
  return root


def createTree(arr):
  root = None

  for x in arr:
    root = insertNode(root, (x, 1))

  return root


def searchNode(root, x):
  if root == None or root.key[0] == x:
    return root

  if x < root.key[0]:
    return searchNode(root.left, x)

  return searchNode(root.right, x)


n = int(input())

# professor''s list
pList = []
pSet = set()
for i in range(n):
  # pList.append(int(input()))
  pSet.add(int(input()))

m = int(input())
# student's list
sList = []
for i in range(m):
  sList.append(int(input()))

# Create tree with student's list to have randomness


def main(sList, pList):
  root = createTree(sList)

  counter = 0
  for l in pList:
    res = searchNode(root, l)
    if res != None:
      counter += res.key[1]
  print(counter)

# with student list as tree
# createTree: O(MlogM)
# Search:  + NlogM
# Total O(MlogM + NlogM)

# with prof list as tree
# createTree: O(NlogN) => N*2 due to 1 side tree like linkedList
# Search:  MlogN  => M*N
# total O(NlogN + MlogN) => O(N*2 + M*N)

# Hash table: O(M+ N)


# Binary Search: MlogN


def main2(sList, pSet):
  # pSet = set(pList)

  counter = 0
  for x in sList:
    if x in pSet:
      counter += 1
  print(counter)


# main(sList, pList)

main2(sList, pSet)
