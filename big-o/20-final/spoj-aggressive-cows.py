# https: // www.spoj.com/problems/AGGRCOW/
def isPossible(stalls, m, c):
  cur = stalls[0]
  for i in range(len(stalls)):
    if stalls[i] - cur >= m:
      cur = stalls[i]
      c -= 1
      if c == 1:
        return True
  return False


def solve():
  n, c = map(int, input().split())

  stalls = [int(input()) for _ in range(n)]
  stalls.sort()

  l = 0
  r = 10**9

  while l <= r:
    m = (l + r)//2
    xx = isPossible(stalls, m, c)
    if xx:
      l = m + 1
    else:
      r = m - 1

  print(r)


def main():
  t = int(input())

  for _ in range(t):
    solve()


main()
