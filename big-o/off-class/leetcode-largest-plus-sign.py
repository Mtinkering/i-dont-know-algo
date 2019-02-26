# 1. What's new
# DP
# 2. Why couldnt I solve if it's nothing new
# Didnt think further how to improve from bruteforce
# Bruteforce: calculate on the fly, but erase the result
# Instead we could calculate and cache that.
# https: // leetcode.com/problems/largest-plus-sign/


class Solution:
  def orderOfLargestPlusSign(self, n, mines):
    """
    :type N: int
    :type mines: List[List[int]]
    :rtype: int
    """
    arr = [[1]*n for i in range(n)]
    m = 0
    for x, y in mines:
      arr[x][y] = 0

    dp = [[0]*n for i in range(n)]

    for i in range(n):
      count = 0
      for j in range(n):
        if arr[i][j] == 1:
          count = count + 1
        else:
          count = 0
        dp[i][j] = count
      count = 0
      for j in range(n-1, -1, -1):
        if arr[i][j] == 1:
          count = count + 1
        else:
          count = 0
        dp[i][j] = min(dp[i][j], count)

    for j in range(n):
      count = 0
      for i in range(n):
        if arr[i][j] == 1:
          count = count + 1
        else:
          count = 0
        dp[i][j] = min(dp[i][j], count)

      count = 0
      for i in range(n-1, -1, -1):
        if arr[i][j] == 1:
          count = count + 1
        else:
          count = 0
        dp[i][j] = min(dp[i][j], count)

        m = max(m, dp[i][j])

    return m
