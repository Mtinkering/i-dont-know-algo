# choose random element x = A[i]
# = {
#   left: all less than x
#   right: greater than or equal
# }
# This is quick selecting by a pivot x

# Ideally, in first iteration I will run n times, in the second iteration I will n/2 times, in the third iteration I will run n/4...., and I have to do logN iterations. so sum(n + n/2 + n/4 + ...) = O(n). But in worst case, I have to run sum(n + n - 1 + n - 2 + ....) = O(n ^ 2) where I have to do N iterations

# Compared to quick sort,
# Because in the quicksort, you have to take care of two sides of the pivot. But in quickselect, you only focus on the side the targe object should be. So, in optimal case, the running time of quicksort is (n + 2 * (n/2) + 4 * (n/4)...), it has logn iterations. Instead, the running time of quickselect would be(n + n/2 + n/4 + ...) it has logn iterations as well. Therefore, the running time of quicksort is O(nlogn), instead, the running time of quickselect of quickselect is O(n). Thank you for your comments.

# Quick select
# n + n/2 + n/4 + .. + 1  = 2n => O(n)


def kClosest(points, K):
  length = len(points)
  l = 0
  r = length - 1

  while l <= r:
    # m is the index at which all items on the left are less than it
    # items on the right are greater than or equal to it
    m = partition(points, l, r)
    if m + 1 == K:
      break
    elif m + 1 < K:
      # If not enough, then we need to take some more from the right
      l = m + 1
    else:
      r = m - 1

  # At this point, K items on the left are already sorted
  return points[:K]

# Random pick a pivot. From there split the arr into less than it and greater than it
# The items ARE NOT SORTED, just that they are splited into 2 halves


def partition(arr, l, r):
  # Choose a pivot
  ol = l
  pivot = distance(arr[l])
  l += 1

  while True:
    while l < r and distance(arr[l]) < pivot:
      l += 1
    while l <= r and distance(arr[r]) >= pivot:
      r -= 1
    if l >= r:
      break
    # Swap. At this point,
    # l is pointing to the one greater than or equal pivot
    # r is pointing to the one smaller
    arr[l], arr[r] = arr[r], arr[l]

  arr[l], arr[ol] = arr[ol], arr[l]

  return r


def distance(p):
  return p[0]*p[0] + p[1]*p[1]
