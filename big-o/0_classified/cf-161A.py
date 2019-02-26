n, m, x, y = map(int, input().split())

sizes = list(map(int, input().split()))
vests = list(map(int, input().split()))

answers = []
k = 0
for i in range(n):
  s = sizes[i]
  
  for j in range(k, m, 1):
    v = vests[j]
    if (v >= s - x and v <= s + y):
      answers.append([i, j])
      k = j + 1
      break
    elif (v < s - x):
      k = j + 1
    elif (v > s + y):
      break
    if (k == m):
      break


print(len(answers))
for answer in answers:
  print(answer[0] + 1, answer[1] + 1)

# size 1, v=1 >= 1 and <= 1 => answers[[0, 0]]
# size 2, v=3 >=2 and <= 2
# size 2, v = 
#O( m *n)

while i < n and j < m:
    if sizes[i] - x <= vests[j] <= sizes[i] + y:
        answers.append((i, j))
        i += 1
        j += 1
    elif vests[j] < sizes[i] - x:
        j += 1
    else:
        i += 1

print(len(answers))
for answer in answers:
  print(answer[0] + 1, answer[1] + 1)
