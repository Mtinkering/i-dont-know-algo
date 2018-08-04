'''
' Steven Aug 4 2018
' https://www.spoj.com/problems/PRO/
' Priority Queue
' Idea: The idea is to keep track what has been deleted
' Complexities: ?
'''
import heapq
import sys


class Scanner:
  def __init__(self, istream):
    self.tokenizer = Scanner.__tokenizer__(istream)

  def __tokenizer__(istream):
    try:
      for line in istream:  # line = '2'
        for token in line.strip().split():
          yield token
    except EOFError:
      exit()

  def next(self):
    return self.tokenizer.__next__()


sc = Scanner(sys.stdin)

n = int(sc.next())

qMax = []
qMin = []
cost = 0
numbers = [0]*(10**6+1)

for _ in range(n):
  k = int(sc.next())

  for i in range(k):
    x = int(sc.next())
    numbers[x] += 1

    heapq.heappush(qMin, x)
    heapq.heappush(qMax, -x)

  while numbers[qMin[0]] == 0:
    heapq.heappop(qMin)
  smallest = heapq.heappop(qMin)
  numbers[smallest] -= 1

  while numbers[-qMax[0]] == 0:
    heapq.heappop(qMax)
  largest = -heapq.heappop(qMax)
  numbers[largest] -= 1

  cost += largest - smallest
print(cost)
