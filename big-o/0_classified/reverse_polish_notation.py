def process(s):
  stack = []
  arr = s.split()
  print(arr)
  for c in arr:
    if c in '+-*/':
      x1 = stack.pop()
      x2 = stack.pop()
      x = 0
      if c == '+':
        x = x2 + x1
      elif c == '-':
        x = x2 - x1
      elif c == '*':
        x = x2 * x1
      elif c == '/':
        x = x2 / x1
      stack.append(x)
    else:
      stack.append(int(c))
  return stack[0]


print(process('15 7 1 1 + - / 3 * 2 1 1 + + -'))
