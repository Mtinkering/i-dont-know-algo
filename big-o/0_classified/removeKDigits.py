def removeKdigits(self, num, k):
  if len(num) == k:
    return "0"

  st = []

  for i in range(len(num)):
    c = int(num[i])

    while k != 0 and len(st) != 0 and st[-1] > c:
      st.pop()
      k -= 1

    if len(st) != 0 or c != 0:
      st.append(c)

  while k != 0:
    st.pop()
    k -= 1

  return "0" if len(st) == 0 else "".join(map(str, st))


print(removeKdigits(1, "1432219", 3))
print(removeKdigits(1, "10", 2))
print(removeKdigits(1, "10200", 1))
print(removeKdigits(1, "10200", 2))
print(removeKdigits(1, "123345", 5))
print(removeKdigits(1, "123345", 6))
print(removeKdigits(1, "7654331", 6))
print(removeKdigits(1, "1230", 3))

0
0
0
0
0
0
1
2
0



