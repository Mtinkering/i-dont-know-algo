n = int(input())
l = [0] + list(map(int, input().strip().split()))
# arr = [0] + [1]*n

# for i in range(1, n + 1, 1):
#   j = i - l[i]
#   if (j < 1):
#     j = 1

#   for a in range(j, i, 1):
#     arr[a] = 0

# print(sum(arr))

# n = 10
# l = [0, 1,1,3,0,0,0,2,1,0,3]

totalDead = 0
currentLow = n + 1
currentHigh = n + 1
for i in range(n, 0, -1):
  low = max(1, i - l[i])
  high = i - 1

  # valid
  if (low <= high):
    # 3 possbible cases:
    # low, high out of range of current
    # high is in the middle, low is out
    # both are inside
    if (low <= currentLow and high >= currentLow):
      currentLow = low
    elif (high < currentLow):
      totalDead += currentHigh - currentLow + 1
      currentLow = low
      currentHigh = high
      

totalDead += currentHigh - currentLow + 1

# + 1 because the last guy is always alive
print(n - totalDead + 1)
