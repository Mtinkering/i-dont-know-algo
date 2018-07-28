'''
' Steven Jul 29 2018
' https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/activity/
' Priority Queue
'''

import queue


class PQEntry:
  def __init__(self, id, deltaScore, newScore):
    self.id = id
    self.deltaScore = deltaScore
    self.newScore = newScore

  def __lt__(self, other):  # want it to appear on top
    if self.deltaScore != other.deltaScore:
      return self.deltaScore < other.deltaScore
    else:
      return self.id < other.id


n = int(input())


q = queue.PriorityQueue()


for i in range(n):
  id, z, p, l, c, s = map(int, input().strip().split())

  newScore = p*50 + l*5 + c*10 + s*20

  deltaScore = newScore - z

  q.put(PQEntry(id, deltaScore, newScore))

  if (q.qsize() > 5):
    q.get()


results = []
while q.qsize() != 0:
  element = q.get()
  results.append((element.id, element.newScore))

for i in range(4, -1, -1):
  print(*results[i])
