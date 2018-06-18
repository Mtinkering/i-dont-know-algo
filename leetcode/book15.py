# def isPalindrome(n):
#   if (n < 0):
#     return False

#   s = str(n)
#   l = 0
#   r = len(s) - 1
#   while l < r:
#     if(s[l] == s[r]):
#       l += 1
#       r -= 1
#     else:
#       break
  
#   if (l < r):
#     return False
#   else:
#     return True


# def isPalindrome(n):
#     if (n < 0):
#         return False


#     remainder = n
#     m = 0
#     while remainder != 0:
#         m = m*10 + remainder%10
#         remainder //= 10

#     return m == n

def isPalindrome(n):
    if (n < 0):
        return False

    div = 1
    while (n // div >= 10):
        div *= 10

    while n != 0:
        l = n // div
        r = n % 10
        if (l != r):
            return False
        n = (n%div)// 10
        div /= 100

    return True
print(isPalindrome(121))  # [1,2,4]
print(isPalindrome(122))  # [1,2,4]
print(isPalindrome(-122))  # [1,2,4]
print(isPalindrome(0))  # [1,2,4]
print(isPalindrome(1))  # [1,2,4]
print(isPalindrome(1231))  # [1,2,4]
print(isPalindrome(13531))  # [1,2,4]
print(isPalindrome(1031))  # [1,2,4]
print(isPalindrome(1001))  # [1,2,4]
