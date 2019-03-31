# Task in order of diff


def main():
  n = int(input())
  if n < 3:
    print('NO')
    return
  values = list(map(int, input().split()))

  arr = [i for i in range(n)]
  arr.sort(key=lambda x: values[x])

  ans = [[x + 1 for x in arr]]
  for i in range(1, n):
    cur = arr[i]
    prev = arr[i-1]
    if values[cur] == values[prev]:
      arr[i-1] = cur
      arr[i] = prev
      newList = [x + 1 for x in arr]
      ans.append(newList)

    if len(ans) == 3:
      print('YES')
      for l in ans:
        print(*l)

      return

  print('NO')


main()
