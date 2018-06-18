n = int(input())
arr = list(map(int, input().split()))

answer = []

# for i in range(n):
#   counter = 0
#   for j in range(n):
#     if (j != i):
#       if (arr[i] < arr[j]):
#         counter += 1
#   answer.append(counter + 1)

sortedArr = sorted(arr, reverse=True)
for i in range(n):
  j = 0
  while arr[i] < sortedArr[j]:
    j += 1
  answer.append(j + 1)
print(*answer)


n = int(input())
arr = list(map(int, input().split()))

answer = []

# for i in range(n):
#   counter = 0
#   for j in range(n):
#     if (j != i):
#       if (arr[i] < arr[j]):
#         counter += 1
#   answer.append(counter + 1)

sortedArr = []
for i in range(n):
  sortedArr.append((arr[i], i))
sortedArr = sorted(sortedArr, reverse=True)
res = [0] * n
res[sortedArr[0][1]] = 1
for i in range(1, n):
  if sortedArr[i][0] == sortedArr[i - 1][0]:
    res[sortedArr[i][1]] = res[sortedArr[i - 1][1]]
  else:
    res[sortedArr[i][1]] = i + 1

print(*res)
# for i in range(n):
#   j = 0
#   while arr[i] < sortedArr[j]:
#     j += 1
#   answer.append(j + 1)
# print(*answer)

# 1 2 3 4 5 ... 2000
# 1999 + 1998 + ... + 1 = (1 + 1999) * 1999 / 2

#3 5 3 4 5 -> 5 5 4 3 3

sortedArr = [(3, 0), (5, 1), (3, 2), (4, 3), (5, 4)]
- > [(5, 1), (5, 4), (4, 3), (3, 0), (3, 2)]

res[1] = 1
res[4] = 1
res[(4, 3)[1]] = 2 + 1 = 3
res[(3, 0)[1]] = 3 + 1 = 4
res[(3, 2)[1]] = 4

# sortedArr = sorted(sortedArr, key=lambda x: (x[0], -x[1]))
