# https: // leetcode.com/problems/3sum-with-multiplicity/submissions/

import collections


class Solution(object):
  def threeSumMulti(self, A, target):

    hash = {}

    res = 0
    MOD = 10**9 + 7

    for i, val in enumerate(A):

      res = (res + hash.get(target - val, 0)) % MOD

      for j in range(i):
        temp = A[j] + val

        hash[temp] = hash.get(temp, 0) + 1
    return res

# # Time limit
# class Solution(object):
#   def threeSumMulti(self, A, target):
#     MOD = 10**9 + 7
#     ans = 0
#     A.sort()

#     for i, x in enumerate(A):
#       # We'll try to find the number of i < j < k
#       # with A[j] + A[k] == T, where T = target - A[i].

#       # The below is a "two sum with multiplicity".
#       T = target - A[i]
#       j, k = i+1, len(A) - 1

#       while j < k:
#         # These steps proceed as in a typical two-sum.
#         if A[j] + A[k] < T:
#           j += 1
#         elif A[j] + A[k] > T:
#           k -= 1
#         # These steps differ:
#         elif A[j] != A[k]:  # We have A[j] + A[k] == T.
#           # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
#           # And similarly for "right".
#           left = right = 1
#           while j + 1 < k and A[j] == A[j+1]:
#             left += 1
#             j += 1
#           while k - 1 > j and A[k] == A[k-1]:
#             right += 1
#             k -= 1

#           # We contributed left * right many pairs.
#           ans += left * right
#           ans %= MOD
#           j += 1
#           k -= 1

#         else:
#           # M = k - j + 1
#           # We contributed M * (M-1) / 2 pairs.
#           ans += (k-j+1) * (k-j) // 2
#           ans %= MOD
#           break

#     return ans


class Solution(object):
  def threeSumMulti(self, A, target):

    hash = {}

    res = 0
    MOD = 10**9 + 7

    for i, val in enumerate(A):

      res = (res + hash.get(target - val, 0)) % MOD

      for j in range(i):
        temp = A[j] + val

        hash[temp, hash.get(temp, 0) + 1]
    return res

# # Time limit
# class Solution(object):
#   def threeSumMulti(self, A, target):
#     MOD = 10**9 + 7
#     ans = 0
#     A.sort()

#     for i, x in enumerate(A):
#       # We'll try to find the number of i < j < k
#       # with A[j] + A[k] == T, where T = target - A[i].

#       # The below is a "two sum with multiplicity".
#       T = target - A[i]
#       j, k = i+1, len(A) - 1

#       while j < k:
#         # These steps proceed as in a typical two-sum.
#         if A[j] + A[k] < T:
#           j += 1
#         elif A[j] + A[k] > T:
#           k -= 1
#         # These steps differ:
#         elif A[j] != A[k]:  # We have A[j] + A[k] == T.
#           # Let's count "left": the number of A[j] == A[j+1] == A[j+2] == ...
#           # And similarly for "right".
#           left = right = 1
#           while j + 1 < k and A[j] == A[j+1]:
#             left += 1
#             j += 1
#           while k - 1 > j and A[k] == A[k-1]:
#             right += 1
#             k -= 1

#           # We contributed left * right many pairs.
#           ans += left * right
#           ans %= MOD
#           j += 1
#           k -= 1

#         else:
#           # M = k - j + 1
#           # We contributed M * (M-1) / 2 pairs.
#           ans += (k-j+1) * (k-j) // 2
#           ans %= MOD
#           break

#     return ans


# class Solution:
#   def threeSumMulti(self, A, target):
#     """
#     :type A: List[int]
#     :type target: int
#     :rtype: int
#     """
#     MOD = 10**9 + 7

#     count = [0]*101

#     for x in A:
#       count[x] += 1

#     ans = 0

#     #x != y != z
#     for x in range(101):
#       for y in range(101):
#         z = target - x - y
#         if 0 <= z <= 100:
#           if x < y and y < z:
#             ans += (count[x]*count[y]*count[z]) % MOD
#           elif x == y and y < z:
#             ans += ((count[x]*(count[x]-1)//2)*count[z]) % MOD
#           elif x < y and y == z:
#             ans += ((count[y]*(count[y]-1)//2)*count[x]) % MOD
#           elif x == y and y == z:
#             ans += ((count[y]*(count[y]-1)*(count[y]-2)//6)) % MOD
#         # print(x, y, z, ans)
#     return ans


# # Find 2 sums of x + y = target - z
# class Solution(object):
#   def threeSumMulti(self, A, target):
#     MOD = 10**9 + 7
#     count = collections.Counter(A)
#     keys = sorted(count)

#     ans = 0

#     # Now, let's do a 3sum on "keys", for i <= j <= k.
#     # We will use count to add the correct contribution to ans.
#     for i, x in enumerate(keys):
#       T = target - x
#       j, k = i, len(keys) - 1
#       while j <= k:
#         y, z = keys[j], keys[k]
#         if y + z < T:
#           j += 1
#         elif y + z > T:
#           k -= 1
#         else:  # x+y+z == T, now calculate the size of the contribution
#           if i < j < k:
#             ans += count[x] * count[y] * count[z]
#           elif i == j < k:
#             ans += count[x] * (count[x] - 1) / 2 * count[z]
#           elif i < j == k:
#             ans += count[x] * count[y] * (count[y] - 1) / 2
#           else:  # i == j == k
#             ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6

#           j += 1
#           k -= 1

#     return ans % MOD

# # 4 cases:
# # if x = y = z: then get 3 out of n => C 3 of n = n! / ((n-k)!k!)
# # if x = y < z: then (get 2 out of count(x) ) * count(z)
# # if x < y = z: then get 2 out of count(y)   * count(x)
# # if all different: then count(x) * count(y) * count(z)


# class Solution:
#   def threeSumMulti(self, A, target):
#     """
#     :type A: List[int]
#     :type target: int
#     :rtype: int
#     """
#     MOD = 10**9 + 7
#     ans = 0
#     count = collections.Counter(A)

#     keys = sorted(count)

#     for x in keys:
#       for y in keys:
#         z = target - x - y

#         if 0 <= z <= 100 and x < y and y < z:
#           ans += (count[x]*count[y]*count[z]) % MOD
#         elif 0 <= z <= 100 and x == y and y < z:
#           ans += ((count[x]*(count[x]-1)//2)*count[z]) % MOD
#         elif 0 <= z <= 100 and x < y and y == z:
#           ans += ((count[y]*(count[y]-1)//2)*count[x]) % MOD
#         elif 0 <= z <= 100 and x == y and y == z:
#           ans += ((count[y]*(count[y]-1)*(count[y]-2)//2)) % MOD
#         # print(x, y, z, ans)
#     return ans


sol = Solution()

print(sol.threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8))
print(sol.threeSumMulti([1, 1, 2, 2, 2, 2], 5))
print(sol.threeSumMulti([16, 51, 36, 29, 84, 80, 46, 97, 84, 16], 171))
# print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
# print(sol.twoSum(-2, [-1, 0, 1, 2, -1, -4]))
# print(sol.twoSum(-2, {-4: 1, -1: 2, 0: 1, 1: 1, 2: 1}))
