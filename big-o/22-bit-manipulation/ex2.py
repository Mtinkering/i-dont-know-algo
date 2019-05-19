def convertToBase2(m):
  res = []

  while m != 0:
    d = m % 2

    res.append(d)

    m = m // 2

  # res.reverse()

  return res


def convertToBase2_v2(m):
  res = []

  while m != 0:
    d = m & 1

    res.append(d)

    m >>= 1

  res.reverse()

  return res


def solve(n, m):
  arr = convertToBase2(m)
  ans = []

  for i in range(len(arr)-1, -1, -1):
    if arr[i] == 1:
      ans.append('(' + str(n) + '<<' + str(i) + ')')

  print(' + '.join(ans))


def main():
  t = int(input())

  for i in range(t):
    n, m = map(int, input().split())
    solve(n, m)


# main()
print(convertToBase2(10))
print(convertToBase2_v2(10))
