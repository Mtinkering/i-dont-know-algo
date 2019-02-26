# ----------
n = int(input())

a = list(map(int, input().split()))
M = dict()

res = 0
for i in range(n):
  for j in range(31):
    res += M.get(2 ** j - a[i], 0)  # a[i] = 5 -> 3, 11, 27, ...
  M[a[i]] = M.get(a[i], 0) + 1

print(res)

# ------------

input()
arr = list(map(int, input().split()))


def sumK(arr, k):
  m = {}  # store the frequency of complements
  total = 0

  for number in arr:
    if number in m:
      total += m[number]

    compl = k - number
    m[compl] = m.get(compl, 0) + 1

  return total


def sumK(arr, k):
  m = {}  # store the frequency each element
  total = 0

  for number in arr:
    total += m.get(k - number, 0)
    m[number] = m.get(number, 0) + 1

  return total


k = 1
ans = 0
while k <= 2*10**9:  # O(30)
  ans += sumK(arr, k)  # O(n)
  k *= 2

print(ans)
