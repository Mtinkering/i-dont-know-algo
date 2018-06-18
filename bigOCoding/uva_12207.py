import queue


def solveOneCase(p, c, counter):
  print('Case ' + str(counter) + ':')

  q = queue.Queue()

  for i in range(min(p, c)):
    q.put(i+1)
  # for i in range(p):
  #   q.put(i+1)

  for _ in range(c):
    cmd = input()
    if cmd == 'N':
      k = q.get()
      print(k)
      q.put(k)
    else:
      e = int(cmd.split()[1])
      mq = queue.Queue()
      mq.put(e)
      for i in range(q.qsize()):
        k = q.queue[i]
        if (k != e):
          mq.put(k)

      q = mq


p, c = map(int, input().split())
counter = 1
while p != 0:
  solveOneCase(p, c, counter)
  counter += 1
  p, c = map(int, input().split())

# c*min(p, c)
