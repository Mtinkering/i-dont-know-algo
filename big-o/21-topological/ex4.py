import queue


def topologicalSort(graph, result):
  n = len(graph)

  indegree = [0]*n
  zeroIndegree = queue.Queue()
  rank = {}

  for i in range(n):
    for v in graph[i]:
      indegree[v] += 1

  for i in range(n):
    if indegree[i] == 0:
      rank[i] = 1
      zeroIndegree.put(i)

  while not zeroIndegree.empty():
    u = zeroIndegree.get()
    result.append([rank[u], u])

    for v in graph[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        rank[v] = rank[u] + 1
        zeroIndegree.put(v)


def solve(test):
  print("Scenario #" + str(test+1) + ":")

  n, r = map(int, input().split())

  graph = [[] for i in range(n)]

  for _ in range(r):
    r1, r2 = map(int, input().split())

    graph[r2].append(r1)

  result = []
  topologicalSort(graph, result)

  result.sort()

  for pair in result:
    print(*pair)


def main():
  t = int(input())

  for test in range(t):
    solve(test)


main()
