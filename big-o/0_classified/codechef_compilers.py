
# https: // www.codechef.com/status/COMPILER


def solve():
  s = input()
  st = []
  prefixSize = 0

  for i in range(len(s)):
    if s[i] == '<':
      st.append(i)
    else:
      if len(st) > 0:
        open = st.pop()

        if len(st) == 0:
          prefixSize = i + 1
      else:
        break

      return prefixSize


t = int(input())

for _ in range(t):
  print(solve())
