def binarySearch(arr, key):
  left = 0
  right = len(arr) - 1
  found = False

  while left <= right and not found:
    middle = (left + right) // 2

    if (key < arr[middle]):
      right = middle - 1
    elif (key > arr[middle]):
      left = middle + 1
    else:
      found = True

  return found

# print(binarySearch([1,2,4,5,7], 6))
print(binarySearch([1], 1))
print(binarySearch([1, 2], 1))
