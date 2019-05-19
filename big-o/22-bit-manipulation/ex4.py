def solve():
  n, k = map(int, input().split())

  arr = []

  for i in range(n):
    s = input()
    arr.append(int(s, base=2))

  ans = 11
  for j in range(2**k):
    validChoice = True

    for i in arr:
      if j & i == 0:
        validChoice = False
        break

    if validChoice:
      cnt = 0

      while j != 0:
        if j & 1 == 1:
          cnt += 1

        j >>= 1

      ans = min(ans, cnt)

  print(ans)


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
