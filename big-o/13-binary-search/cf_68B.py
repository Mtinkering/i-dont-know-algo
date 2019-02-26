# http: // codeforces.com/problemset/problem/68/B

def isPossibleWithAmount(arr, e, k):
  total = 0

  for number in arr:
    if number > e:
      total += number - e
    else:
      x = (e - number)*100/(100-k)
      total -= x

  return total >= 0


n, k = map(int, input().split())

arr = list(map(int, input().split()))

left = min(arr)
right = max(arr)


0 -> 1000
1000 / 2 ^ k ~ 10 ^ -7

k ~ log2(10 ^ 10) ~ 33

while abs(left - right) > 10**(-7):
  mid = (right + left)/2

  test = isPossibleWithAmount(arr, mid, k)
  # print(left, mid, right, test)

  if test == True:
    left = mid
  else:
    right = mid


print(left)


# left right mid
# 1     4     2.5
