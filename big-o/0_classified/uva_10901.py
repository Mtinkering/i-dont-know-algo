import queue

def ferryLoading(n,t,m):

  # q of time onboard
  answer = [0]*m
  qLeft = queue.Queue()
  qRight = queue.Queue()
  ferryOnboard = queue.Queue()
  ferryTime = 0
  currentSide = 'left'
  rivers = {'left': qLeft, 'right': qRight}
  for i in range(m):

    t1, side = input().split()
    t1 = int(t1)

    rivers[side].put((t1, i))
  
  while m > 0:
    #Loading
    while rivers[currentSide].qsize() != 0 and rivers[currentSide].queue[0][0] <= ferryTime and ferryOnboard.qsize() < n:
        ferryOnboard.put(rivers[currentSide].get())

    #Unloading
    if ferryOnboard.qsize() != 0:
      ferryTime += t
      currentSide = 'right' if currentSide == 'left' else 'left'
      while ferryOnboard.qsize() != 0:
        car = ferryOnboard.get()
        answer[car[1]] = ferryTime
        m -= 1
    else:
      if qLeft.qsize() != 0 and qRight.qsize() != 0:
        if qLeft.queue[0][0] < qRight.queue[0][0]:
          if currentSide == 'left':
            ferryTime = max(ferryTime, qLeft.queue[0][0])
          else:
            ferryTime = max(ferryTime, qLeft.queue[0][0]) + t
            currentSide = 'left'
        elif qLeft.queue[0][0] > qRight.queue[0][0]:
          if currentSide == 'left':
            ferryTime = max(ferryTime, qRight.queue[0][0]) + t
            currentSide = 'right'
          else:
            ferryTime = max(ferryTime, qRight.queue[0][0])
        else:
          ferryTime = max(ferryTime, qRight.queue[0][0])
      elif qLeft.qsize() == 0:
        if currentSide == 'left':
          ferryTime = max(ferryTime, qRight.queue[0][0]) + t
          currentSide = 'right'
        else:
          ferryTime = max(ferryTime, qRight.queue[0][0])
      else:
        if currentSide == 'right':
          ferryTime = max(ferryTime, qLeft.queue[0][0]) + t
          currentSide = 'left'
        else:
          ferryTime = max(ferryTime, qLeft.queue[0][0])

  #           time = 0
  # while qLeft.qsize() or qRight.qsize():
  #   if qLeft.empty():
  #     next = qRight.queue[0][0]
  #   else:
  #     if qRight.empty():
  #       next = qLeft.queue[0][0]
  #     else:
  #       next = max(qLeft.queue[0][0], qRight.queue[0][0])
  #   time = max(time, next)
  #   cnt = 0
  #   while rivers[currenSide].qsize() and rivers[currentSize].queue[0][0] <= time and cnt < n:
  #     answer[rivers[currentSide].get()[1]] = time + t
  #     cnt += 1
  #   time += t
  #   currentSide = 'right' if currentSide == 'left' else 'left'

  for k in answer:
    print(k)
x = int(input())
for i in range(x):
  n, t, m = map(int, input().split())
  ferryLoading(n,t,m)
  if i != x - 1:
    print('')
