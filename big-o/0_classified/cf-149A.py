k = int(input())
arr = list(map(int, input().split()))

sortedMonthGrowth = sorted(arr, reverse=True)

if (k == 0):
  print(0)
else:
  i = -1
  total = 0
  while total < k:
    i += 1
    if (i > 11):
      break
    total += sortedMonthGrowth[i]

  if (i == 12 and total < k):
    print(-1)
  else:
    # because index 0
    print(i+1)
