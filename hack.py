

class Node:
  def __init__(self):
    self.endWord = False
    self.children = {}

# add(1) # 0
# add(2) # 10
# add(3) # 110

# add(2) # 00
# add(2) # 01
# add(2) # 0
# YES
# 0000
# 0001
# 0010
# 0011
# 0100
# 0101
# 0110
# 0111
# 1000
# 1001

# 0000
# 0001
# 0010
# 0011
# ...


def addNode(root, num, s, changed):  # num = 1, 2 ,3
  if root.endWord == True:
    return ''

  if num == 0:
    root.endWord = True

    if changed == False:
      return ''
    return s

  cur = root

  c = '0'

  if c not in cur.children:
    #  or cur.children[c].endWord == False:
    cur.children[c] = Node()
    changed = True
    return addNode(cur.children[c], num - 1, s + c, changed)

    #   c = '1'

    #   if c not in cur.children:

    #     temp = addNode(cur.children[c], num - 1, s + c)

    #     if temp == '':
    #       return ''
  else:
    temp = addNode(cur.children[c], num - 1, s + c, changed)

    if temp == '':
      c = '1'

      if c not in cur.children:
        cur.children[c] = Node()
        changed = True
        return addNode(cur.children[c], num - 1, s + c, changed)

      else:
        temp = addNode(cur.children[c], num - 1, s + c, changed)

        if temp == '':
          return ''
        else:
          return temp

    else:
      return temp

  # elif cur.children[c].endWord == True:
  #   c = '1'

  #     cur.children[c] = Node()

  #   elif cur.children[c].endWord == True:
  #     return ''

  # cur = cur.children[c]

  # cur.endWord = True

  return s

# def main():
#   n = int(input())

#   nums = map(int, input().split())
#   res = []

#   root = Node()
#   # print(res)

#   for num in nums:

#     s = addNode(root, num, '')
#     # print(s)
#     if s == '':
#       return []

#     res.append(s)
#   return res


def main():
  n = int(input())

  nums = list(map(int, input().split()))

  res = []
  words = {}
  root = Node()
  for num in nums:
    words[num] = words.get(num, 0) + 1

    if words[num] > 2**(num):
      return []

  for num in nums:
    # print(num)
    s = addNode(root, num, '', False)
    res.append(s)

  return res


ans = main()

if len(ans) == 0:
  print('NO')
else:
  print('YES')
  print('\n'.join(ans))


# def main():
#   n = int(input())

#   nums = map(int, input().split())

#   res = []
#   words = {}

#   for num in nums:
#     words[num] = words.get(num, 0) + 1

#     if words[num] > 2**(num):
#       return []


#   for num in nums:
#     s = addNode(root, num, '')

#     res.append(s)

#   return res

# ans = main()

# if len(ans) == 0:
#   print('NO')
# else:
#   print('YES')
#   print('\n'.join(ans))
