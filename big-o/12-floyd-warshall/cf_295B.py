def floydWarshall(graph):
  n = len(graph)

  distance = [[0]*n for i in range(n)]

  for i in range(n):
    for j in range(n):
      distance[i][j] = graph[i][j]

  for k in range(n):
    for i in range(n):
      for j in range(n):
        if distance[i][k] + distance[k][j] < distance[i][j]:
          distance[i][j] = distance[i][k] + distance[k][j]
  return distance


n = int(input())

graph = [None]*n

for i in range(n):
  graph[i] = list(map(int, input().split()))

deleted = list(map(int, input().split()))


result = []

remaining = [[0]*n for i in range(n)]

for i in range(n-1, -1, -1):
  v = deleted[i]-1
  print(v)
  for j in range(n):
    remaining[j][v] = graph[j][v]
    remaining[v][j] = graph[v][j]
  print(remaining)
  distance = floydWarshall(remaining)
  print(distance)
  total = 0
  for k in range(n):
    for l in range(n):
      total += distance[k][l]

  result.append(total)
print(result)

# print(deleted)
# print(graph)


# ===  Solution ===
# http: // codeforces.com/contest/295/problem/B

def floydWarshall(distance, k):
  n = len(distance)
  for i in range(n):
    for j in range(n):
      if distance[i][k] + distance[k][j] < distance[i][j]:
        distance[i][j] = distance[i][k] + distance[k][j]


n = int(input())

graph = [None]*n

for i in range(n):
  graph[i] = list(map(int, input().split()))


deleted = list(map(int, input().split()))
vertices = []

result = []

distance = graph

for i in range(n-1, -1, -1):
  v = deleted[i]-1

  vertices.append(v)

  floydWarshall(graph, v)

  total = 0

  for k in vertices:
    for l in vertices:
      total += distance[k][l]

  result.append(total)


print(*result[::-1])
