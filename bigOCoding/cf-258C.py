n = int(input())
arr = list(map(int, input().split()))

validNumbers = set()
toFix = []

for number in arr:
  if (1 <= number <= n and number not in validNumbers):
    validNumbers.add(number)
  else:
    toFix.append(number)

toFix.sort()
total = 0
i = 0
for p in range(1, n + 1, 1):
  if (p not in validNumbers):
    total += abs(p - toFix[i])
    i += 1
    validNumbers.add(p)


print(total)
