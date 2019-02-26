# Print lexigraphical order
words = ['abd', 'abc', 'efg']

words.sort()
print(*words)


class Node():
  def __init__(self):
    self.children = {}
    self.endOfWord = False

# True means there is prefix


def addPass(trie, pw):
  tmp = trie

  for c in pw:
    if c not in tmp.children:
      tmp.children[c] = Node()
    tmp = tmp.children[c]
  tmp.endOfWord = True


def inOrderTraversal(root, s):
  if root.endOfWord == True:
    print(s)

  keys = root.children.keys()

  for key in sorted(keys):
    inOrderTraversal(root.children[key], s + key)


trie = Node()


for word in words:
  addPass(trie, word)

inOrderTraversal(trie, '')
