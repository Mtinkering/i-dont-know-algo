def binarySearch(a, left, right, x):
  while left <= right:
    mid = (left + right)//2

    if a[mid] == x:
      return mid
    elif x > a[mid]:
      left = mid + 1
    else:
      right = mid - 1

  return -1


def binarySearch(a, left, right, x):
  if left <= right:
    mid = (left + right)//2

    if a[mid] == x:
      return mid

    if x > a[mid]:
      return binarySearch(a, mid + 1, right, x)

    return binarySearch(a, left, mid - 1, x)

  return -1
