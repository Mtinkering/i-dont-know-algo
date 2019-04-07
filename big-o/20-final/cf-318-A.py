n, k = map(int, input().split())

m = (n+1)//2

if k <= m:
  print(1 + (k-1)*2)
else:
  print(2*(k-m))
