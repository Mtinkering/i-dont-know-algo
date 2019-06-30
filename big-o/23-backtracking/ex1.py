def solve(arr, l, r, result):
  print(l, r, result)
  if len(result) == 3:
    print(*result)
  else:
    for i in range(l, r):
      result.append(arr[i])
      solve(arr, i+1, r, result)
      result.pop()

# N * (N - 1) * (N - 2) * (N - 3) * (N - 4) * (N - 5)
# O(N^6)


# arr: 1, 2, 3, 4, 5, 6, 7

# [ , , , , , ]
# |
# v
# [1, , , , , ] -> [1,2,,,,,] -> [1,2,3, ,,] -> [1,2,3,4,5,6]

# |
# v


# Ck/n = n!/k!/(n-k)!

solve([1, 2, 3, 4, 5], 0, 5, [])
