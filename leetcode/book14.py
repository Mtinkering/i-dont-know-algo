def plusOne(digits):
  n = len(digits)
  overflow = False
  for i in range(n-1, -1, -1):
    if (digits[i] != 9):
      digits[i] += 1
      break
    else:
      digits[i] = 0
      if (i == 0):
        overflow = True

  if (overflow == True):
    digits.append(0)
    digits[0] = 1

  return digits

print(plusOne([1,2,3])) # [1,2,4]
print(plusOne([4,3,2,1])) # [1,2,4]
print(plusOne([0])) # [1,2,4]
print(plusOne([9])) # [1,2,4]
print(plusOne([9,9,9])) # [1,2,4]
print(plusOne([9,9,8])) # [1,2,4]
print(plusOne([1,9,9])) # [1,2,4]