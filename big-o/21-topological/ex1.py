def dfs(graph, result, visited, u):
  visited[u] = 1

  for v in sorted(graph[u], reverse=True):
    # for v in graph[u]:
    if visited[v] == 1:
      return False

    if visited[v] == 0:
      if dfs(graph, result, visited, v) == False:
        return False

  visited[u] = 2
  result.append(u)
  return True


def main():
  n, m = map(int, input().split())

  graph = [[] for i in range(n)]

  for i in range(m):
    x, y = map(int, input().split())

    graph[x-1].append(y-1)

  result = []

  # 0: not visited. 1: visiting. 2: visited
  visited = [0]*n

  flag = True
  for i in range(n-1, -1, -1):
    # for i in range(n):
    if visited[i] == 0:
      if dfs(graph, result, visited, i) == False:
        flag = False
        break

  if flag:
    result.reverse()
    for i in result:
      print(i+1, end=' ')
  else:
    print("Sandro fails.")


main()


# 1 -> 3 -> 5 -> 7
# 8 -> 4 -> 6

# result: 6 4 8
# 8 4 6
