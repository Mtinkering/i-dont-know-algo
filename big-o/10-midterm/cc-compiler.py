t = int(input())

def validate(s):
  ''' return number'''
  stack = []
  counter = 0
  n = len(s)
  answer = [-1]*n
  for i in range(n):
    c = s[i]
    if c == '<':
      stack.append(i)
    elif c == '>':
      if len(stack) != 0:
        j = stack.pop()
        answer[i] = 1
        answer[j] = 1
      else:
        break
  k = 0
  while k <= n - 1 and answer[k] == 1:
    counter += 1
    k += 1

  return counter

for _ in range(t):
  print(validate(input().strip()))


// Efficient
def validate(s):
  ''' return number'''
  stack = []
  counter = 0
  n = len(s)
  answer = [-1]*n
  stlen = 0
  ans = 0
  for i in range(n):
    c = s[i]
    if c == '<':
      #       stack.append(i)
      stlen += 1
    elif c == '>':
      stlen -= 1
      if stlen == 0:
        ans = i + 1
      if stlen < 0:
        break
#       if len(stack) != 0:
#         j = stack.pop()
#         answer[i] = 1
#         answer[j] = 1
#       else:
#         break
  return ans
  k = 0
  while k <= n - 1 and answer[k] == 1:
    counter += 1
    k += 1

  return counter
