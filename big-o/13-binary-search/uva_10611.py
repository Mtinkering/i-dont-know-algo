import bisect

# def findLastSmaller(arr, k):
#   left = 0
#   right = len(arr) - 1

#   while left <= right:
#     mid = (left + right)//2

#     if arr[mid] == k:
#       right = mid - 1
#       if mid == left or arr[mid - 1] < k:
#         break
#     elif arr[mid] > k:
#       right = mid - 1
#     else:
#       left = mid + 1

#   return right

k = 0
[1, 2, 2, 3] . = > -1
k = 4 = > index = 3


def findLastSmaller(arr, k):
  left = 0
  right = len(arr) - 1
  res = -1

  while left <= right:
    mid = (left + right)//2

    if arr[mid] < k:
      res = mid
      left = mid + 1
    else:
      right = mid - 1

  return res


def findFirstGreater(arr, k):
  left = 0
  right = len(arr) - 1
  res = -1

  while left <= right:
    mid = (left + right)//2

    if arr[mid] > k:
      res = mid
      right = mid - 1
    else:  # smaller or equal
      left = mid + 1

  return res


n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for k in list(map(int, input().split())):
  # lower = bisect.bisect_left(arr, k) - 1
  # upper = bisect.bisect_right(arr, k)

  lower = findLastSmaller(arr, k)
  upper = findFirstGreater(arr, k)

  if lower == -1:
    print('X', arr[upper])
  elif upper == -1:
    print(arr[lower], 'X')
  else:
    print(arr[lower], arr[upper])

# O(n+qlog(n))
