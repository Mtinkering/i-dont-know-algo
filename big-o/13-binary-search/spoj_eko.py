# https: // www.spoj.com/problems/EKO/

n, m = map(int, input().split())

arr = list(map(int, input().split()))

left = 0
right = 10**9

while left <= right:
  mid = (left + right) // 2
  total = sum([a - mid for a in arr if a > mid])

  if total >= m:
    left = mid + 1
  elif total < m:
    right = mid - 1

print(right)


# sortedArray = sorted(arr)

# ans = -1
# for x in range(min(arr), max(arr)+1):
#   total = totalWood(arr, x)
#   # print(total)
#   if total >= m:
#     ans = x
# print(ans)
