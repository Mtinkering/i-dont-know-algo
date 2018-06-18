def cleanUp(s):
  l = ''
  for c in s:
    if c.isalpha():
      l += c.lower()
  return l


s1 = cleanUp(input())
s2 = cleanUp(input())
s3 = cleanUp(input())

possibleStrings = [s1 + s2 + s3, s1 + s3 + s2, s2 +
                   s1 + s3, s2 + s3 + s1, s3 + s1 + s2, s3 + s2 + s1]

n = int(input())

for _ in range(n):
  s = cleanUp(input())

  if s in possibleStrings:
    print('ACC')
  else:
    print('WA')
