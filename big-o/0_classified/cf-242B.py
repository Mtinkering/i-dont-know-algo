n = int(input())
left = [None]*n
right = [None]*n

for i in range(n):
  left[i], right[i] = map(int, input().split())

answer = -1

minL = 10**9 + 1
for i in range(n):
  if (left[i] < minL):
    minL = left[i]

maxR = 0
for i in range(n):
  if (right[i] > maxR):
    maxR = right[i]


for i in range(n):
  if (left[i] == minL and right[i] == maxR):
    answer = i + 1

print(answer)
