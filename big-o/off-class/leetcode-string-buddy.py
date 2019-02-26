def buddyStrings(self, A, B):
  """
  :type A: str
  :type B: str
  :rtype: bool
  """
  if len(A) != len(B):
    return False

  diff = []
  # str2 = ''
  hash1 = {}
  for i in range(len(A)):
    if A[i] in hash1:
      hash1[A[i]] += 1
    else:
      hash1[A[i]] = 1

    if A[i] != B[i]:
      diff.append(i)
      # str2 += B[i]

  if len(diff) == 0:
    # How to check if there is duplicate
    for value in hash1.values():
      if (value > 1):
        return True
    return False

  return len(diff) == 2 & & A[diff[0]] == B[diff[1]] & & A[diff[1]] == B[diff[0]]


print(buddyStrings(1, 'ab', 'ab'))
