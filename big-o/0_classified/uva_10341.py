import math


def predicate(p, q, r, s, t, u, x):
  return p*math.e**(-x) + q*math.sin(x) + r*math.cos(x) + s*math.tan(x) + t*x*x + u


def solve(p, q, r, s, t, u):
  p0 = predicate(p, q, r, s, t, u, 0)
  p1 = predicate(p, q, r, s, t, u, 1)

  if p0*p1 > 0:
    print('No solution')
    return

  low = 0
  high = 1

  while high - low >= 10**(-10):
    mid = (low + high) / 2

    if predicate(p, q, r, s, t, u, mid)*p1 > 0:
      high = mid
    else:
      low = mid

    # if predicate(p, q, r, s, t, u, mid) > 0:
    #   if p1 > 0:
    #     high = mid
    #   else:
    #     low = mid
    # else:
    #   if p1 > 0:
    #     low = mid
    #   else:
    #     high = mid

  print(f'{high:.4f}')
  # print(f'{low:.4f}')
  # print(f'{high:.4f}')
  # print("%.5f" % high)


while True:
  try:
    p, q, r, s, t, u = map(int, input().split())
    solve(p, q, r, s, t, u)
  except Exception:
    break
