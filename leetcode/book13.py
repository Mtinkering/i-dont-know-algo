def reverse(n):
  arr = []
  remainder = abs(n)
  m = 0
  while remainder != 0:
    m = m*10 + remainder%10
    remainder = remainder//10

  if (n < 0):
    m = -m

  if (m < -2**31 or m > 2**31 - 1):
    m = 0
  return m

print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(10))
print(reverse(100))
print(reverse(0))
print(reverse(1000000003))
print(reverse(-1000000003))
