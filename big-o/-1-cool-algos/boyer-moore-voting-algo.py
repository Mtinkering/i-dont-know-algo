# This algo helps to find the majority element in the array in O(1) space and O(n) time

# The intuition behind it is, if majority element adds one, minority reduces one, then the sum eventually
# will be greater than zero
# So when the current sum is zero, it means the prefix can be ignored and we can focus on the suffix

arr = [7, 7, 5, 7, 5, 1 | 5, 7 | 5, 5, 7, 7 | 7, 7, 7, 7]


def majorityElement(self, nums: List[int]) -> int:
  candidate = None
  count = 0

  for num in nums:
    if count == 0:
      candidate = num

      count += 1
    elif num == candidate:
      count += 1
    else:
      count -= 1

  return candidate

# Super cool idea
