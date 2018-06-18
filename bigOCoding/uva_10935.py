import queue


def solveOneCase(n):
  q = queue.Queue()
  discard = []
  for i in range(1, n+1, 1):
    q.put(i)

  while (q.qsize() >= 2):
    discard.append(q.get())
    q.put(q.get())

  if (len(discard) == 0):
    print('Discarded cards:')
  else:
    print('Discarded cards: ' + ', '.join(map(str, discard)))
  print('Remaining card: ' + str(q.get()))


n = int(input())
while n != 0:
  solveOneCase(n)
  n = int(input())
