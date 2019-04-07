1 + 3 + 5 + 7 + 9 + ... + n = (n + 1) ^ 2 / 4
1 + 2 + 3 + ... + n = n * (n + 1) / 2


1 + 3 + 5 = (5+1) ^ 2/4 = 9


s = 8


(n+1)

(n + 1) ^ 2 / 4 = 8
= > n = 4.6

n = 5


r = (n+1)//2 = 3
c = (n+1)//2 = 3

val = (3+1) ^ 2/4 = 4
c r
1 3 9
2 3 8
3 3 7
3 2 6
3 1 5


(n + 1) ^ 2 / 4 = 25
= > n = 9

r = 5
c = 5


x, y =
val = 16
5, 1 .: 17
5, 2: 18
5, 3: 19

n = 9: max = 25
  min = 17

r = 5

# From 0, N
corner = max - r + 1 = 21

if s > corner:
  x = max - s + 1
  y = N
  (x, y)
else:
  x = N
  y = s - min + 1
  (x, y)


s = 15

n = 7: max = 16
  min = 10

r = 5

# From 0, N
corner = max - r + 1 = 21

if s > corner:
  if max % 2 == 0:
    x = N
    y = s - min + 1
    (x, y)
  else:
    x = max - s + 1
    y = N
    (x, y)
else:
  if max % 2 == 1:
    x = N
    y = s - min + 1
    (x, y)
  else:
    x = max - s + 1
    y = N
    (x, y)
