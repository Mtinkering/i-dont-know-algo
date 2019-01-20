# https: // icpcarchive.ecs.baylor.edu/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 3803


class Node:
  def __init__(self):
    self.child = {}
    self.end = False


def addNode(root, w):
  cur = root
  added = False
  for c in w:
    if c not in cur.child:
      cur.child[c] = Node()
      added = True
    cur = cur.child[c]
  cur.end = True

  return added


def addNewNode(root, w):
  print("word = " + w)
  cur = root
  counter = 0
  queue = [root]

  while len(queue) != 0:
    temp = []
    for cur in queue:
      for child in cur.child:
        node = cur.child[child]
        temp.append(node)
        res = addNode(node, w)
        if res == True:
          counter += 1
    print(temp)
    queue = temp

  return counter


def solve(p, s):
  prefix = Node()
  for _ in range(p):
    w = input()

    addNode(root, w[:k])

  counter = 0
  for _ in range(s):
    w = input()

    for l in range(0, len(w)):
      counter += addNewNode(root, w[l:])

  print(counter)


def main():
  p, s = map(int, input().split())

  while p != 0 or s != 0:
    solve(p, s)
    p, s = map(int, input().split())


main()
