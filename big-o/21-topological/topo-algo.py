def dfs(u, graph, visited, result):
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
