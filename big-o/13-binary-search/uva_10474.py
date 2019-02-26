
def binarySearch(a, left, right, x):
  if left <= right:
    mid = (left + right)//2

    if (mid == left or a[mid - 1] < x) and a[mid] == x:
      return mid
    elif x > a[mid]:
      return binarySearch(a, mid + 1, right, x)
    else:
      return binarySearch(a, left, mid - 1, x)

  return -1


def solve(n, q, t):
  arr = []

  for _ in range(n):
    arr.append(int(input()))

  arr.sort()

  print("CASE# " + str(t) + ":")
  for _ in range(q):
    x = int(input())
    i = binarySearch(arr, 0, len(arr) - 1, x)

    if i == -1:
      print(str(x) + " not found")
    else:
      print(str(x) + " found at " + str(i+1))


n, q = map(int, input().split())
t = 1
while not (n == 0 and q == 0):
  solve(n, q, t)

  t += 1
  n, q = map(int, input().split())


#O(t*(nlogn + qlogn))
# O(t*(n*q))
