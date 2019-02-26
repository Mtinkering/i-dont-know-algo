l, r, x, y, k = map(int, input().split())

x1 = k*x
y1 = k*y

iX = max(l, x1)
iY = min(r, y1)

lower = iX//k if iX % k == 0 else iX//k + 1
higher = iY // k

if (higher - lower >= 0):
  print('YES')
else:
  print('NO')