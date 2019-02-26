
t = int(input())

for dt in range(t):
  ans = []
  title = input().upper()
  m, n, b = map(int, input().split())

  cost = {}

  for i in range(m):
    name, price = input().split()
    cost[name] = int(price)

  for i in range(n):
    name = input()
    k = int(input())
    totalCost = 0

    for j in range(k):
      requirement, x = input().split()

      price = cost.get(requirement, 0)

      totalCost += int(x)*price

    # Within the budget
    if totalCost <= b:
      ans.append((name, totalCost))

  print(title)
  if len(ans) != 0:
    ans.sort(key=lambda x: (x[1], x[0]))
    for k, c in ans:
      print(k)
  else:
    print("Too expensive!")

  print()
