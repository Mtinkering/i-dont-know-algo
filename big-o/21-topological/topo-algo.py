# 3 colors of a node:
# RED: Visited
# YELLOW: VISTING
# GREEN: Not Visited

# One important thing in topo sort is: If we care about the order of the output, for example, if a and b have no relation,
# the order should be the same as input, then using kahn with priority queue is easier
# But then the complexity is higher, due to maintaining the PQ

# Using # 0: not visited. 1: visiting. 2: visited
# visited = [0]*n
# This allows to check if there is a cycle


def dfs(u, graph, visited, result):
  visited[u] = True
  for v in graph[u]:
    if not visited[v]:
      dfs(v, graph, visited, result)

  result.append(u)


def topologicalSort(graph, result):
  visited = [False]*len(graph)

  for i in range(len(graph)):
    if not visited[i]:
      dfs(i, graph, visited, result)

  result.reverse()


def main():

  V, E = map(int, input().split())
  graph = [[] for i in range(V)]
  result = []

  for _ in range(E):
    u, v = map(int, input().split())
    graph[u].append(v)

  topologicalSort(graph, result)
  print(*result)
