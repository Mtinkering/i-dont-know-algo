import queue

n = int(input())

adj = {}
score = {}

for i in range(n):
  names = input().split()

  for n in names:
    if n not in adj:
      adj[n] = set()

    for m in names:
      if n != m:
        adj[n].add(m)

    score[n] = -1


def bfs(adj, score):
  Isenbaev = 'Isenbaev'

  if Isenbaev not in score:
    return

  q = queue.Queue()

  q.put(Isenbaev)

  score[Isenbaev] = 0

  while not q.empty():
    u = q.get()

    for v in adj[u]:
      if score[v] == -1:
        score[v] = score[u] + 1
        q.put(v)


bfs(adj, score)

arr = sorted(score.items())

for t in arr:
  if t[1] == -1:
    print(t[0] + " undefined")
  else:
    print(t[0] + ' ' + str(t[1]))
