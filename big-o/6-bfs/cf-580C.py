from queue import Queue

n, m = map(int, input().split())

arr = list(map(int, input().strip().split()))
cats = [-1]*n

graph = [[] for i in range(n)]

for i in range(n-1):
  u, v = map(int, input().split())
  graph[u-1].append(v-1)
  # graph[v-1].append(u-1)
q = Queue()
q.put(0)
cats[0] = arr[0]

while not q.empty():
  u = q.get()

  for v in graph[u]:
    # print(v, cats)
    if cats[v] == -1:
      if arr[v] == 0:
        q.put(v)
        cats[v] = 0
      else:
        cats[v] = cats[u] + 1
        if cats[v] <= m:
          q.put(v)
counter = 0
# print(graph)
# print(cats)
for i in range(n):
  if i != 0 and len(graph[i]) == 0 and 0 <= cats[i] <= m:
    counter += 1
print(counter)
