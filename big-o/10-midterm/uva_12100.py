import queue
# Printer queue


class PQEntry:
  def __init__(self, value):
    self.value = value

  def __lt__(self, other):
    return self.value > other.value


def solve():
  n, m = map(int, input().split())

  arr = list(map(int, input().split()))

  pq = queue.PriorityQueue()
  q = queue.Queue()

  for index, priority in enumerate(arr):
    pq.put(PQEntry(priority))  # O(logN)
    q.put((priority, index))

  minutes = 0

  while True:
    currentMax = pq.queue[0].value

    j = q.get()

    if j[0] < currentMax:
      q.put(j)
    else:
      pq.get()
      minutes += 1

      if j[1] == m:
        break

  print(minutes)


t = int(input())

for _ in range(t):
  solve()


# nlogn
