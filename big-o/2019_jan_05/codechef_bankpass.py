# https: // www.codechef.com/problems/BANKPASS/
##################
# Correct        #
##################
# class Node():
#   def __init__(self):
#     self.children = {}
#     self.endOfWord = False

# # True means there is prefix
# def addPass(trie, pw):
#   tmp = trie
#   oldPath = True

#   for c in pw:
#     if c not in tmp.children:
#       tmp.children[c] = Node()
#       oldPath = False

#     tmp = tmp.children[c]

#     if tmp.endOfWord == True:
#       return True

#   tmp.endOfWord = True


#   return oldPath

# # if __name__ == "__main__":
# n = int(input())

# trie = Node()

# ans = 'non vulnerable'

# for i in range(n):
#   pw = input()

#   res = addPass(trie, pw)

#   if res == True:
#     ans = 'vulnerable'
#     break

# print(ans)


##################
# Wrong          #
##################
class Node():
  def __init__(self):
    self.children = {}
    self.endOfWord = False


def addPass(trie, pw):
  tmp = trie
  oldPath = True

  for c in pw:
    if c not in tmp.children:
      tmp.children[c] = Node()
    #   oldPath = False

    tmp = tmp.children[c]

    if tmp.endOfWord == True:
      return False

  tmp.endOfWord = True

  return oldPath


# if __name__ == "__main__":
n = int(input())

trie = Node()

ans = 'non vulnerable'

for i in range(n):
  pw = input()

  res = addPass(trie, pw)

  if res == False:
    ans = 'vulnerable'
    break

print(ans)
