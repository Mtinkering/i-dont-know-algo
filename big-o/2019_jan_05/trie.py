class Node:
  def __init__(self):
    self.countWord = 0  # End of word when countWord == 1. Số luong từ kết thúc ở vị trí này
    self.child = dict()

# Trie operation
# Add
# Search
# Delete
# Keys have to be an order of some kind
# Time Complexity O(string_length)
# Trùng: tiền tố.
# Mỗi nút có thể có 26 nút con (nếu dùng ASCII)


def addWord(root, s):
  tmp = root

  for ch in s:
    if ch not in tmp.child:
      tmp.child[ch] = Node()
    tmp = tmp.child[ch]


def findWord(root, s):
  tmp = root

  for ch in s:
    if ch not in tmp.child:
      return False

    tmp = tmp.child[ch]

  return tmp.countWord > 0

# delete until seeing the new word


def removeWord(root, s, level, len):
  # if root == None:
  #   return False

  # if level == len:
  #   if root.countWord > 0:
  #     root.countWord -= 1
  #     return True

  #   return False
  pass
