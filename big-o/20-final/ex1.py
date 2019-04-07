

# read only array
# n integers from 1 -> n
# each integer appears exactly one, except A which appears twice, and B is missing
# Find A, B

# [3 1 2 5 3]
# -> 3 4
# [1 2 3 3 5] # sort
# nlogn
# [1 2 3 3 5]
# [1 2 3 3 4]

# map(1,2,3,5) # 4
# [1 2 4 4 5]

# def findAB(arr):
#   hash = {}
#   a = -1
#   b = -1
#   for num in arr:
#     if num not in hash:
#       hash[num] = 0

#     hash[num] += 1
#     if hash[num] == 2:
#       a = num

#   for i in range(1, n+1):
#     if i not in hash:
#       b = i
#   return (a, b)

# print(findAB([3, 1, 2, 5, 3]))

# time and space: O(n)


def findMisingNumer(arr):
  n = len(arr)
  t1 = n*(n+1)//2
  t2 = sum([i*i for i in range(1, n+1)])
  n * (n + 1) * (2 * n + 1) / 6
  s1 = sum(arr)
  s2 = sum([i*i for i in arr])

  d1 = s1 - t1
  d2 = s2 - t2

  d3 = d2//d1

  a = (d3 + d1)//2
  b = (d3 - d1)//2

  return (a, b)


print(findMisingNumer([3, 1, 2, 5, 3]))

# [3 1 2 5 3]
# [1 2 3 4 5]

# 3 -> 2 -> 1 -> 3
# arr[0] = 3
# arr[2] = 2
# arr[1] = 1
# [1 2 3 4 5] # 15
#   # 14
# [1 2 3 5 5] # 16


# 1 -> 5: mid is 3
# greater than 3: 5
# 1 2


# 3 1 2 5 3 # 14

# A - B ? 3 - 4

# A - B = sum(arr) - sum(1 -> n)
# 2(A - B) = sum(arr) + sum(arr) - 2*sum(1->n) = A + A - B

# A ^ 2 - B ^ 2 = 1^2 + 2^2 + 3^2 + 3^2 + 5^2 - 1^2 + 2^2 + 3^2 + 4^2 + 5^2 = 9 - 16 = -7
# (A-B)(A+B) = -7
# A + B = 7
# A - B = -1
# 2A = 6 => A = 3

# 3: 11
#     12
# 1  10 11
# 2  8 9
# 5  3 4
# 3  0 1


# A - B = -1
# 2A - B =
