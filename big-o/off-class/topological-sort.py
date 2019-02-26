# Wrong iterative version.
# def dfs(src, visited, stack, graph):
#   visited[src] = True
#   st = [src]

#   while st:
#     top = st.pop()
#     stack.append(top)

#     for neighbor in graph[top]:
#       if visited[neighbor] == False:
#         visited[neighbor] = True
#         st.append(neighbor)

#         stack.append(neighbor)


def dfs(src, visited, stack, graph):
  visited[src] = True

  stack.append(src)
  for neighbor in graph[src]:
    if visited[neighbor] == False:
      dfs(neighbor, visited, stack, graph)

  stack.append(src)


def topologicalSort(graph):
  onPath = [False for i in range(len(graph))]
  visited = [False for i in range(len(graph))]

  for i in range(len(graph)):
    if visited[i] == False:
      dfs(i, visited, onPath, graph)

  print(*reversed(onPath))
  print(*onPath[::-1])


def main():
  n = 5
  graph = [[] for i in range(n)]

  graph[2].append(3)
  graph[3].append(0)
  graph[4].append(3)
  graph[0].append(1)
  graph[1].append(4)

  print(graph)
  topologicalSort(graph)


main()
