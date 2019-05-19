def main():
  t = int(input())

  for _ in range(t):
    n = int(input())

    arr = list(map(int, input().split()))

    if n & 1 == 0:
      print(0)
    else:
      res = 0
      for i in range(n):
        # if i % 2 == 0:
        if i & 1 == 0:
          res ^= arr[i]

      print(res)


main()
