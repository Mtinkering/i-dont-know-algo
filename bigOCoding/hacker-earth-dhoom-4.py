from queue import Queue

s, key = map(int, input().split())
n = int(input())
arr = list(map(int, input().split()))

q = Queue()
visited = [-1]*100001

q.put(s)
visited[s] = 0
answer = -1

while q.empty() == False:
  u = q.get()
#   print(q.queue)
  for num in arr:
    v = (num*u) % 100000
    if v == key:
      answer = visited[u] + 1
      break

    if visited[v] == -1:
      visited[v] = visited[u] + 1
      q.put(v)

  if answer != -1:
    break

print(answer)

# bfs
