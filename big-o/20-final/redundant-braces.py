# ((a + b)): 1


# (a + (a + b)): 0


(a + b) -> 0

# ( )


def braces(self, A):
  st = []

  for c in A:
    if c == ')':
      if st[-1] == '(':
        return 1

      hasOperator = False
      while st[-1] != '(':
        el = st.pop()
        if el in ('+', '*', '-', '/'):
          hasOperator = True

      if hasOperator == False:
        return 1

      st.pop()

    else:
      st.append(c)

  return 0


(a)
(0, 2)


def braces(self, s):
  last_pair = (-1, -1)
  st = []
  for i in range(len(s)):
    if s[i] == '(':
      st.append(i)
    elif s[i] == ')':
      if last_pair == (st[-1] + 1, i - 1):
        -> ((....))
          return 1
      last_pair = (st.pop(), i)
    else:
      last_pair = (i, i)
  return 0
