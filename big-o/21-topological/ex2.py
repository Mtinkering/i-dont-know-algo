# http: // bigocoder.com/courses/ORANGE01/ORANGE01_LEC01/ORANGE_L01P02/statement
# def topologicalSort2(graph, result):
#   n = len(graph)

#   indegree = [0]*n

#   zeroIndegree = queue.Queue()

#   for u in range(n):
#     for v in graph[u]:
#       indegree[v] += 1

#   for u in range(n):
#     if indegree[u] == 0:
#       zeroIndegree.put(u)

#   while not zeroIndegree.empty():
#     u = zeroIndegree.get()
#     result.append(u)

#     for v in graph[u]:
#       indegree[v] -= 1

#       if indegree[v] == 0:
#         zeroIndegree.put(u)

#   return len(result) == n


def dfs(src, graph, visited, result):
  visited[src] = 1

  for v in graph[src]:
    if visited[v] == 0:
      dfs(v, graph, visited, result)

  result.append(src)


def topologicalSort(graph, result):
  visited = [0]*len(graph)

  for i in range(len(graph)):
    if visited[i] == 0:
      dfs(i, graph, visited, result)
  result.reverse()


def main():
  n, k = map(int, input().split())

  graph = [[] for i in range(n)]
  # parent = {}
  for i in range(k):
    data = list(map(int, input().split()))

    w = data[0]

    for j in range(w):
      v = data[j+1]
      graph[i].append(v-1)
      # parent[v-1] = i

  result = []
  topologicalSort(graph, result)

  ans = [0]*n
  for i in range(n):
    u = result[i]
    if i == 0:
      ans[u] = 0
    else:
      ans[u] = result[i-1] + 1

  for i in ans:
    print(i)


main()
