def solve(arr, l, r, result):
  print(l, r, result)
  if len(result) == 3:
    print(*result)
  else:
    for i in range(l, r):
      result.append(arr[i])
      solve(arr, i+1, r, result)
      result.pop()


solve([1, 2, 3, 4, 5], 0, 5, [])
