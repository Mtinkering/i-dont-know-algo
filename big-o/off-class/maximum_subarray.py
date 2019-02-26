def maxSubarray(arr):

  # Want to find  value
  maxValue = float('-inf')
  currentSum = 0

  # Want to find subarray?
  maxSubArray = []
  currentMax = []

  # Want to find starting and ending indices? Using Stack
  k = 0
  j = 0
  st = []
  finalStack = []

  # Want to find starting and ending indices?
  currentI = -1
  currentJ = 0
  finalI = 0
  finalJ = 0
  for i, element in enumerate(arr):
    currentSum += element
    currentMax.append(element)
    st.append(i)
    currentJ = i
    # print(currentMax, currentSum)
    if currentSum > maxValue:
      maxValue = currentSum

      # Must copy by value, not reference
      maxSubArray = currentMax[:]
      finalStack = st[:]


      finalI = min(currentI+1, currentJ)
      finalJ = currentJ
    
    # Reset
    if currentSum < 0:
      currentSum = 0
      currentMax = []
      st = []
      currentI = i

  # print(finalStack)
  j = finalStack.pop()
  if len(finalStack) == 0:
    k = j
  else:
    while len(finalStack) != 0:
      k = finalStack.pop()
  return maxValue, maxSubArray, k, j, finalI, finalJ


print(maxSubarray([2]))
print(maxSubarray([-32]))
print(maxSubarray([1, 1, 1, 1, 1]))
print(maxSubarray([2, -3, 3, 5]))
print(maxSubarray([2, -3, 3, 5, -7]))
print(maxSubarray([2, -3, 3, 5, -7, 6, 3]))
print(maxSubarray([-1, -2, -3, -4, -5]))
print(maxSubarray([-5, -4, -3]))
print(maxSubarray([-1, 2, 3, -4, -5]))
print(maxSubarray([-1, 2, 3, -4, 5]))
