def distance(x, y):
  return (x*x + y*y) ** 0.5


n, s = map(int, input().split())

locations = {}

for i in range(n):
  x, y, k = map(int, input().split())

  d = distance(x, y)

  locations[d] = locations.get(d, 0) + k

arr = sorted(locations.items())

ans = -1
for d, k in arr:
  if s + k >= 10**6:
    ans = d
    break
  s += k


print(ans)
