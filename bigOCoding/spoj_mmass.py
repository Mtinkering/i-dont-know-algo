s = input().strip()

def mmass(s):
  stack = []
  table = {'C': 12, 'H': 1, 'O': 16}
  for c in s:
    if c in 'CHO':
      stack.append(table[c])
    elif c in '23456789':
      stack.append(stack.pop()*int(c))
    elif c == '(':
      stack.append(c)
    else:
      temp = 0
      while stack[-1] != '(':
        temp += stack.pop()
      stack.pop()
      stack.append(temp)

  return sum(stack)


print(mmass(s))
