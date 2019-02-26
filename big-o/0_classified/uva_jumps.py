

def checkTheJumps(arr, k):
  # if len(arr) == 1:
  #   return arr[0] == k

  for i in range(len(arr) - 1):
    feetToJump = arr[i+1] - arr[i]
    if feetToJump > k:
      return False
    elif feetToJump == k:
      k -= 1

  return True


def solve():
  n = int(input())

  arr = [0] + list(map(int, input().split()))

  left = 1
  right = 10**7
  res = 10**7

  while left <= right:
    mid = (left + right)//2

    isPossible = checkTheJumps(arr, mid)
    # print(mid, isPossible)

    if isPossible == True:
      res = mid
      right = mid - 1
    else:
      left = mid + 1

  return res


def main():
  t = int(input())

  for i in range(t):
    result = solve()

    print('Case ' + str(i+1) + ': ' + str(result))


main()
