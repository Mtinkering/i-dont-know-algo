def solve():
  n = int(input())

  arr = list(map(int, input().split()))

  powerOfTwo = 1

  for _ in range(31):
    subset = 2**31 - 1

    for k in arr:
      if k & powerOfTwo != 0:
        subset &= k

    if subset == powerOfTwo:
      print('YES')
      return

    powerOfTwo <<= 1

  print('NO')


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
