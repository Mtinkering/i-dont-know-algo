

# d #Min distance

# i = 3 1 4 2 0
# v = 2 5 7 8 20 . => d = min(2, 12) = 2

# 20 5 8 2 7
# 20 - 5 = 15
# 20 - 8 = 12
# 5 - 2 = 3
# 8 - 7 = 1
#     20
#   5
# 2   8
#   7
#   n*log
# key = -1
#     1
#   0   2

#       root(key)
#   left    right

INF = float('inf')


class Node:
  def __init__(self, key):
    self.key = key
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


def searchFirstGreaterNode(root, p):
  if root == None:
    return INF

  if p < root.key:
    return min(root.key, searchFirstGreaterNode(root.left, p))

  if p > root.key:
    return searchFirstGreaterNode(root.right, p)

#     11 . <- 3
#   8   20
# 2
#   5


# def minimumLoss(price):
#   arr = [(price[i], i) for i in range(len(price))]

#   arr.sort()

#   d = float('inf')

#   for i in range(len(arr) - 1):
#     if arr[i][1] > arr[i+1][1]:
#       d = min(d, arr[i+1][0] - arr[i][0])

#   return d

def minimumLoss(price):
  root = None
  d = float('inf')

  for p in price:
    firstBigger = searchFirstGreaterNode(root, p)
    # print(firstBigger, p)
    d = min(d, firstBigger - p)

    root = insertNode(root, p)

  return d

  20


print(minimumLoss([11, 20, 8, 2, 5, 3]))

# def minimumLoss(price):
#   arr = [(price[i], i) for i in range(len(price))]

#   x(i) > y(j), i < j
#   i < k < j, x(i) > z(k) &&  z(k) > y(j)

#   d = x - y
#   a[i][1] > a[i + 1][1]:
#   a[i][0] a[i + 1][0]

#   arr.sort()

#   d = float('inf')

#   for i in range(len(arr) - 1):
#     if arr[i][1] > arr[i+1][1]:
#       d = min(d, arr[i+1][0] - arr[i][0])

#   return d

# import re


# def strFilter(string):
#   return re.sub(r"[^A-Za-z]+", ' ', string).lower()

# # Binary Search tree
# class Node:
#   def __init__(self, w):
#     self.key = w
#     self.left = None
#     self.right = None

# # abc-cdf

# # abc
# # cdf

# def insertNode(root, word):
#   if root == None:
#     return Node(word)
#   if word < root.key:
#     root.left = insertNode(root.left, word)
#   elif word > root.key:
#     root.right = insertNode(root.right, word)
#   return root

# # O(line*(characters + n*log(n)*len(word)))

# root = None

# while True:
#   try:
#     line = input()

#     newLine = strFilter(line)
#     words = newLine.split()

#     for word in words:
#       if len(word) > 0:
#         root = insertNode(root, word)

#   except Exception:
#     break


# def treeTraversal(root):
#   if root == None:
#     return

#   treeTraversal(root.left)

#   print(root.key)

#   treeTraversal(root.right)


# treeTraversal(root)


# # Add then sort
# # wordSet = set()
# # while True:
# #   try:
# #     line = input()

# #     words = map(strFilter, line.strip().split())

# #     for word in words:
# #       if len(word) > 0:
# #         wordSet.add(word)

# #   except Exception:
# #     break

# # for word in wordSet:
# #   print(word)
