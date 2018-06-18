
# #time that task finishes
# q = [11, 19, -1, 19 + 2, 21 + 1]

# [11, 11 + 8, -1]


# t = 2 + 9 = 11
# [9,] # qSize = 2
# 5 1
# 2 9
# 4 8
# 10 9
# 15 2 # ? how to check 1st task finished. while q.queue[0] = 11 < 15 => get, decrease qSize = 1. put task in q
# 19 1
import sys
input = sys.stdin.readline

n, b = map(int, input().split())
q = queue.Queue()
backOfQueue = 0

for i in range(n):
  t, d = map(int, input().split())

  # Clear tasks in queue at time t
  while not q.empty() and q.queue[0] <= t:
    q.get()

  if q.qsize() <= b:
    if q.qsize() == 0:
      backOfQueue = t + d
    else:
      backOfQueue += d
    q.put(backOfQueue)
    print(backOfQueue, end=' ')
  else:
    print('-1', end=' ')


# while not q.empty():
#   answer.append(q.get())

# print(*answer)


# 2,9
# i:0
# backOfQueue = 2 +9 = 11
# answer [11]
# q(11)

# i = 1; 4, 8
# q(11, 19)
# backOfQueue = 11 + 8 = 19
# answer [11,19]

# i = 2; 10 9
# q(11, 19)
# answer [11,19, -1]
# backOfQueue = 11 + 8 = 19

# i = 3; 15 2
# q(19)
# backOfQueue = 19 + 2 = 21
# q(19, 21)
# answer [11,19, -1, 21]


# i = 4; 19 1
# backOfQueue = 21 + 1 = 22
# q(21,22)
# answer [11,19, -1, 21, 22]


# i = 5; 30 1
# backOfQueue = 30 + 1 = 31
# q(31)
# answer [11,19, -1, 21, 22, 31]
