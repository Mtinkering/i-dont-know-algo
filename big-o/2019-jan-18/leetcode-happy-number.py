class Solution:
  def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    def sumDigit(num):
      total = 0
      while num != 0:
        total += (num % 10)**2
        num = num // 10

      return total

    visited = set()
    visited.add(n)

    while True:
      s = sumDigit(n)
      if s == 1:
        return True
      elif s in visited:
        return False

      visited.add(n)
      n = s
