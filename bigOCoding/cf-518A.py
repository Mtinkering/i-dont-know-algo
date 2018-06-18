s1 = input()

s2 = input()
n = len(s1)
diff = 0

for i in range(n):
  print(ord(s2[i]))
  print(ord(s1[i]))
  diff += (ord(s2[i]) - ord(s1[i])) + diff*(10**i)
  print(diff)
  if diff > 1:
    break

if diff > 1:
  for i in range(n-1, -1, -1):
    if s1[i] != 'z':
      print(s1[:i] + chr(ord(s1[i]) + 1) + 'a'*(n-1-i))
      break

else:
  print('No such string')
