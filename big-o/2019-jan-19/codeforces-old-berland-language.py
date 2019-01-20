import sys
sys.setrecursionlimit(1000000)


class Node:
  def __init__(self):
    self.endWord = False
    self.children = {}


K: average length
O(NlogN*K + N*N*K)
# 0000
# 0001
# 4 0000
# 5 00010
#  0
#  |
#  0
#  |
#  0
# / \
# 0 1
#  /
# 0
# 0010

# 0000
# 00

# 00
# 0000


# # ans:
# YES
# 000000
# 0000110
# 0000111
# 0001000
# 0001001
# 000001
# 0001010
# 0001011
# 0001100
# 0001101
# 0001110
# 0001111
# 0010000
# 0010001
# 0010010
# 0010011
# 0010100
# 0010101
# 000010
# 0010110

# # output
# YES
# 000000
# 000001
# 000010
# 0000110
# 0000111
# 0001000
# 0001001
# 0001010
# 0001011
# 0001100
# 0001101
# 0001110
# 0001111
# 0010000
# 0010001
# 0010010
# 0010011
# 0010100
# 0010101
# 0010110

def addNode(root, num, s, changed):
  if root.endWord == True:
    return ''

  # if len(root.children) == 2:
  #   return ''

  if num == 0:
    root.endWord = True

    if changed == False:
      return ''

    return s

  st = []

  for c in ['0', '1']:
    if c not in root.children:
      root.children[c] = Node()
      changed = True
    temp = addNode(root.children[c], num - 1, s + c, changed)
    if temp != '':
      return temp

  return ''


# def withC(root, num, s, changed):
#   if root.endWord == True:
#     return ''

#   if num == 0:
#     root.endWord = True

#     if changed == False:
#       return ''
#     return s

#   for c in ['0', '1']:
#     if c not in root.children:
#       root.children[c] = Node()
#       changed = True
#     temp = withC(root.children[c], num-1, s+c, changed)
#     if temp != '':
#       return temp

#   return ''


# def addNode(root, num):
#   return withC(root, num, '', False)


# def addNode(root, num):
#   cur = root
#   s = []
#   st = []
#   changed = False
#   c = '0'

#   while num != 0:
#     if c not in cur.children:
#       cur.children[c] = Node()
#       changed = True
#       num -= 1
#       s.append(c)
#       st.append(cur)

#       cur = cur.children[c]
#     else:
#       if cur.children[c].endWord == True:
#         c = '1' if c == '0' else '0'

#         if c not in cur.children:
#           cur.children[c] = Node()
#           changed = True
#           num -= 1
#           s.append(c)
#           st.append(cur)
#           cur = cur.children[c]
#         elif cur.children[c].endWord == True:
#           print('hi')
#           if len(st) > 0:
#             num += 1
#             cur = st.pop()
#             s.pop()
#             c = '1' if c == '0' else '0'
#           else:
#             return ''
#         else:
#           num -= 1
#           s.append(c)
#           st.append(cur)
#           cur = cur.children[c]
#       else:
#         num -= 1
#         s.append(c)
#         st.append(cur)
#         cur = cur.children[c]

#   cur.endWord = True

#   if changed == False:
#     return ''
#   return ''.join(s)


def main():
  n = int(input())

  nums = list(map(int, input().split()))

  sortedNums = []

  for i, num in enumerate(nums):
    sortedNums.append((num, i))

  sortedNums.sort()

  root = Node()

  for num, index in sortedNums:
    s = addNode(root, num, '', False)

    if s == '':
      return []
    nums[index] = s

  return nums


ans = main()

if len(ans) == 0:
  print('NO')
else:
  print('YES')
  print('\n'.join(ans))


####################################

import sys
sys.setrecursionlimit(1000000)


class Node:
  def __init__(self, val):
    self.child = dict()
    self.is_blocked = False
    self.val = val


class Trie:
  def __init__(self):
    self.root = Node('')

  def add(self, length, id, res):
    st = [self.root]
    while length and len(st):
      u = st[-1]
      length -= 1
      if 0 not in u.child:
        u.child[0] = Node('0')
      if not u.child[0].is_blocked:
        st.append(u.child[0])
      else:
        if 1 not in u.child:
          u.child[1] = Node('1')
        if not u.child[1].is_blocked:
          st.append(u.child[1])
        else:
          u.is_blocked = True
          length += 2
          st.pop()
    if length == 0:
      st[-1].is_blocked = True
      res[id] = ''.join(node.val for node in st)
      return True
    return False


if __name__ == "__main__":
  n = int(input())
  a = list(map(int, input().split()))
  a = sorted([(a[i], i) for i in range(n)])

  trie = Trie()
  res = [None] * n
  for length, i in a:
    if not trie.add(length, i, res):
      print('NO')
      exit()

  print('YES')
  for length in res:
    print(length)
