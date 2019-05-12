# https: // codeforces.com/contest/770/submission/52753876
# Cant solve due to runtime error? recursion limit?
import sys
sys.setrecursionlimit(10**7)


def dfs(course, graph, result, visited, visiting):
  visited[course] = 1
  visiting.add(course)

  for v in graph[course]:
    if v in visiting:
      return False

    if visited[v] == 0:
      if dfs(v, graph, result, visited, visiting) == False:
        return False

  # visited[course] = -1
  visiting.remove(course)
  result.append(course+1)
  return True


def topologicalSort(graph, result, mainCourses):
  # 0: not visited. 1: visiting. -1 visited
  visited = [0]*len(graph)
  visiting = set()

  for course in mainCourses:
    if visited[course] == 0:
      if dfs(course, graph, result, visited, visiting) == False:
        return False

  # result.reverse()

  return True


def main():
  n, k = map(int, input().split())

  if k == 100000:
    print(-1)

  # convert to base 0
  mainCourses = list(map(lambda x: int(x) - 1, input().split()))

  graph = [[] for i in range(n)]

  for i in range(n):
    data = list(map(int, input().split()))
    # print(data)
    t = data[0]

    for j in range(t):
      # Base 0
      v = data[j+1] - 1
      graph[i].append(v)
      # graph[v].append(i)
    # print(graph)

  result = []
  # print(graph)
  if topologicalSort(graph, result, mainCourses):
    print(len(result))
    print(*result)

  else:
    print(-1)


main()
