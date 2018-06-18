# from queue import Queue
# q = int(input())
q = 1
numbers = [-1]*(100)

def bfs(n):
  q = [n]
  # q.put(n)

  while len(q) != 0:
    nextLevel = []
    for u in q:
      if u < 10:
        numbers[u] = u
      else:
        s = list(str(u))

        v = 1
        for c in s:
          if int(c) != 0:
            v *= int(c)
        if numbers[v] == -1:
          nextLevel.append(v)
          numbers[u] = v 
    q = nextLevel

for i in range(q):
  # l,r,k = map(int, input().split())
  l,r,k = [22,73,9]
  counter = 0
  for n in range(l,r+1,1):
    if numbers[n] == -1:
      bfs(n)

      if numbers[n] == k:
        counter += 1

  print(counter)
