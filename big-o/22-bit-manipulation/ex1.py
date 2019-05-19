n = int(input())

arr = list(map(int, input().split()))

# prefixSum = [0]*n
zeroes = [0]*n
# prefixSum[0] = arr[0]
zeroes[0] = arr[0] ^ 1

for i in range(1, n):
  # prefixSum[i] = prefixSum[i-1] ^ arr[i]

  zeroes[i] = zeroes[i-1] + (arr[i] ^ 1)

q = int(input())

for i in range(q):
  l, r = map(int, input().split())

  # Base 0:
  l -= 1
  r -= 1

  xor = 0
  nZeroes = 0
  if l > 0:
    # xor = prefixSum[r] ^ prefixSum[l - 1]
    nZeroes = zeroes[r] - zeroes[l-1]
  else:
    # xor = prefixSum[r]
    nZeroes = zeroes[r]

  nOnes = nZeroes - (r - l + 1)
  if nOnes % 2 == 1:
    xor = 1
  else:
    xor = 0

  print(xor, nZeroes)
