# #!/bin/python3

# import os
# import sys

# #
# # Complete the twoStacks function below.
# #


# def twoStacks(x, a, b):
#   total = 0
#   nA = 0
#   counter = 0
#   while nA < len(a):
#     if total + a[nA] <= x:
#       total += a[nA]
#       counter += 1
#       nA += 1
#     else:
#       nA -= 1
#       break

#   answer = counter

#   nB = 0
#   while nB < len(b):
#     total += b[nB]
#     counter += 1
#     while (total > x and nA >= 0):
#       total -= a[nA]
#       nA = - 1
#       counter -= 1

#     if total > x and nA == -1:
#       break

#     answer = max(answer, counter)
#     nB += 1

#   return answer




import os
import sys

#
# Complete the twoStacks function below.
#


def twoStacks(x, a, b):
  print(a)
  print(b)
  total = 0
  nA = -1
  counter = 0
  for i in range(len(a)):
    if total + a[i] <= x:
      total += a[i]
      counter += 1
      nA = i
    else:
      break

  answer = counter

  nB = 0
  while nB < len(b):
    total += b[nB]
    counter += 1
    while nA >= 0:
      total -= a[nA]
      nA -= 1
      counter -= 1

    if total > x and nA == -1:
      break

    answer = max(answer, counter)
    nB += 1

  return answer


# if __name__ == '__main__':

#     g = int(input())

#     for g_itr in range(g):
#         nmx = input().split()

#         n = int(nmx[0])

#         m = int(nmx[1])

#         x = int(nmx[2])

#         a = list(map(int, input().rstrip().split()))

#         b = list(map(int, input().rstrip().split()))

#         result = twoStacks(x, a, b)
#         print(result)


print(twoStacks(5, [17, 12, 11, 15, 11, 13, 18, 17, 12, 11, 18, 13, 11, 14, 13, 11, 15, 16, 11, 17, 12, 15, 15, 18, 19, 11, 19, 19, 14, 10, 15, 13, 12, 18, 19, 15, 14, 19, 13, 16], [10, 11, 11, 11, 17, 14, 12, 12, 13, 13, 12, 15, 11, 19, 15, 10, 10, 14, 10, 16, 16, 17, 10, 10, 15, 19]))
