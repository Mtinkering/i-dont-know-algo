t = int(input())
# 12345
# 543321
# 33
# 12333
# 34 8 10 3 2 80 30 33 35
# [34,8,3,2,1]
# [0, 1, 3, 4,8]
for i in range(t):
  n = int(input())

  nums = list(map(int, input().split()))

  st = []

  for i, val in enumerate(nums):
    if i == 0 or nums[st[-1]] > val:
      st.append(i)

  ans = 0
  for j in range(len(nums) - 1, -1, -1):
    num = nums[j]

    while len(st) != 0 and num >= nums[st[-1]] and j >= st[-1]:
      ans = max(ans, j - st[-1])
      st.pop()

  print(ans)
