
for _ in range(int(input())):
  n, m = map(int, input().split())

  comp = {}
  counter = 0

  for x in list(map(int, input().split())):
    c = m - x

    if c in comp and comp[c] > 0:
      counter += 1
      comp[c] -= 1
    else:
      comp[x] = comp.get(x, 0) + 1

  print(counter)
# O(n*t)


for _ in range(int(input())):
  n, m = map(int, input().split())

  arr = sorted(list(map(int, input().split())))

  left = 0
  right = len(arr) - 1
  counter = 0

  while left < right:
    s = arr[left] + arr[right]

    if s == m:
      counter += 1
      left += 1
      right -= 1
    elif s < m:
      left += 1
    else:
      right -= 1

  print(counter)
O(t*nlogn)

for _ in range(int(input())):
  n, m = map(int, input().split())

  arr = sorted(list(map(int, input().split())))

  left = 0
  right = len(arr) - 1
  counter = 0

  print(counter)
#
