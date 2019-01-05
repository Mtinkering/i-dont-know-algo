# http: // lightoj.com/volume_showproblem.php?problem = 1129


class Node():
  def __init__(self):
    self.child = {}
    self.end = False


def main():
  n = int(input())
  root = Node()
  ans = 'YES'
  for _ in range(n):
    dataset = input()
    flag = add(root, dataset)

    if flag == True:
      ans = 'NO'

  return ans


def add(root, s):
  tmp = root
  newNodeCreated = False

  for c in s:
    if c not in tmp.child:
      tmp.child[c] = Node()
      newNodeCreated = True

    tmp = tmp.child[c]

    # prefix
    if tmp.end == True:
      return True

  if newNodeCreated == False:
    return True

  tmp.end = True

  return False


for i in range(int(input())):
  res = main()
  print('Case ' + str(i+1) + ': ' + res)
