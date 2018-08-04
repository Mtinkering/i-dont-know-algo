'''
' Steven Aug 4 2018
' https://www.codechef.com/problems/RRATING
' Priority Queue
' Idea: The idea is to maintain a min heap that is easy to read
' Complexities: nlogn because we put each element in qMax at least once
'''
import heapq

n = int(input())
qMin = []
qMax = []
counter = 0

for _ in range(n):
  data = list(map(int, input().split()))
  op = data[0]

  if op == 1:
    counter += 1
    k = counter // 3
    val = data[1]

    if len(qMin) < k:
      maxVal = heapq.heappushpop(qMax, -val)
      heapq.heappush(qMin, -maxVal)
    else:
      if k != 0 and val > qMin[0]:
        minVal = heapq.heappushpop(qMin, val)
        heapq.heappush(qMax, -minVal)
      else:
        heapq.heappush(qMax, -val)
  else:
    if len(qMin) == 0:
      print("No reviews yet")
    else:
      print(qMin[0])
