# Use indegree is correct, to deal with order
# (V + E)logV

# DFS wont work (or havent found easy way)
# because
# e -> c -> a
# |>        |^
# b ->     d
# In this case, while working on b, can't stop to switch to c easily
# Same for ex1, must use kahn's algo
import queue


def topo(graph, result, beverages):
  indegree = {}
  zeroIndegree = queue.PriorityQueue()

  for key in beverages.keys():
    indegree[key] = 0

  for key in graph.keys():
    for v in graph[key]:
      indegree[v] += 1

  for key in graph.keys():
    if indegree[key] == 0:
      zeroIndegree.put((beverages[key], key))

  while not zeroIndegree.empty():
    _, u = zeroIndegree.get()
    result.append(u)

    for v in graph[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        zeroIndegree.put((beverages[v], v))


def dfs(src, graph, visited, result):
  visited.add(src)

  for v in graph[src]:
    if v not in visited:
      dfs(v, graph, visited, result)

  result.append(src)


def topologicalSort(beverages, graph, result):
  visited = set()
  l = sorted(beverages.keys(), key=lambda x: beverages[x], reverse=True)

  for beverage in l:
    if beverage not in visited:
      dfs(beverage, graph, visited, result)

  result.reverse()


def solve(n, testNumber):
  graph = {}
  beverages = {}

  for i in range(n):
    name = input()
    graph[name] = []
    beverages[name] = i

  m = int(input())
  for _ in range(m):
    b1, b2 = input().split()

    graph[b1].append(b2)

  for key in graph.keys():
    graph[key].sort(key=lambda x: beverages[x], reverse=True)

  result = []
  topologicalSort(beverages, graph, result)
  # topo(graph, result, beverages)

  ans = ' '.join(result)
  print("Case #" + str(testNumber) + ": Dilbert should drink beverages in this order: " + ans + ".")


def main():
  testNumber = 1
  while True:
    try:
      n = int(input())
      solve(n, testNumber)
      print()
      testNumber += 1
      input()
    except EOFError:
      break


main()
