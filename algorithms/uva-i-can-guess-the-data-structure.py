'''
' Steven Jul 29 2018
' https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3146
' Stack, Queue, Priority Queue
'''

import queue


class PQEntry:
  def __init__(self, value):
    self.value = value

  def __lt__(self, other):
    return self.value > other.value


def solve():
  # Use exception to determine EOF
  try:
    n = int(input())
  except EOFError:
    exit()

  # Try everything
  st = []
  q = queue.Queue()
  pq = queue.PriorityQueue()
  isStack = True
  isQueue = True
  isPriorityQueue = True

  for _ in range(n):
    op, val = map(int, input().split())

    if op == 1:
      if isStack:
        st.append(val)

      if isQueue:
        q.put(val)

      if isPriorityQueue:
        pq.put(PQEntry(val))
    else:
      # Invalid Operation: length is zero or value is not the same
      if isStack and (len(st) == 0 or st.pop() != val):
        isStack = False

      if isQueue and (len(q.queue) == 0 or q.get() != val):
        isQueue = False

      if isPriorityQueue and (len(pq.queue) == 0 or pq.get().value != val):
        isPriorityQueue = False

  if not isStack and not isQueue and not isPriorityQueue:
    print('impossible')
  elif isStack and not isQueue and not isPriorityQueue:
    print('stack')
  elif isQueue and not isStack and not isPriorityQueue:
    print('queue')
  elif isPriorityQueue and not isStack and not isQueue:
    print('priority queue')
  else:
    print('not sure')


while True:
  solve()
