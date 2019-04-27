# We need to use kahn's ago because it's not possible to switch while doing dfs
# O(E+VlogV)
import queue


def topologicalSort(graph, result):
  '''
    return True: cyclic
  '''
  n = len(graph)
  indegree = [0]*n
  zeroIndegree = queue.PriorityQueue()

  for u in range(n):
    for v in graph[u]:
      indegree[v] += 1

  for u in range(n):
    if indegree[u] == 0:
      zeroIndegree.put(u)

  while not zeroIndegree.empty():
    u = zeroIndegree.get()
    result.append(u)

    for v in graph[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        zeroIndegree.put(v)

  return len(result) == n


def main():
  n, m = map(int, input().split())

  graph = [[] for i in range(n)]

  for i in range(m):
    x, y = map(int, input().split())
    graph[x-1].append(y-1)

  result = []
  if topologicalSort(graph, result) == True:
    for i in result:
      print(i+1, end=' ')
  else:
    print("Sandro fails.")


main()
