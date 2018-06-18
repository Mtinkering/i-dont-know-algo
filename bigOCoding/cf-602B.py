n = int(input())
points = list(map(int, input().split()))

arr = [0]*100001

k = 0  # number of distinct data points
maxL = 1
l = 0

for i in range(n):
  p = points[i]

  if arr[p] == 0:
    k += 1
    arr[p] = 1
  else:
    arr[p] += 1

  while k > 2:

    #remove 5
    arr[points[l]] -= 1

    # check if removing the distinct data point
    if (arr[points[l]] == 0):
      k -= 1

    #move left
    l += 1

  maxL = max(maxL, i - l + 1)


print(maxL)
