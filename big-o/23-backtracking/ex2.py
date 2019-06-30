def possibleString(n, h, res, l):
  if h == 0:
    print(''.join(map(str, res)))
  else:
    for i in range(n-1, l-1, -1):
      res[i] = 1
      possibleString(n, h - 1, res, i + 1)
      res[i] = 0


def main():
  t = int(input())

  for _ in range(t):
    input()

    n, h = map(int, input().split())
    res = [0]*n

    possibleString(n, h, res, 0)
    print()


main()
