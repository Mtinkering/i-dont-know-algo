import queue


def topologicalSort(graph, result):
  n = len(graph)
  indegree = [0]*n

  zeroIndegree = queue.Queue()

  for u in range(n):
    for v in graph[u]:
      indegree[v] += 1

  for i in range(n):
    if indegree[i] == 0:
      zeroIndegree.put(i)

  cnt = 0
  while not zeroIndegree.empty():
    u = zeroIndegree.get()
    result.append(u)

    for v in graph[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        zeroIndegree.put(v)

    cnt += 1

  return cnt == n
  # for i in range(V):
  #   if indegree[i] != 0:
  #     return False

  # return True


def main():
  V, E = map(int, input().split())

  graph = [[] for i in range(V)]
  result = []

  for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)

  if topologicalSort(graph, result):
    print(*result)

  else:
    print('No result')
