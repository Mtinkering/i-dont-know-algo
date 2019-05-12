# Cant solve. Too hard
import queue


def topoSort(graph, result):
  n = len(graph)
  indegree = [0]*n

  for i in range(n):
    for v in graph[i]:
      indegree[v] += 1

  zeroDegree = queue.Queue()

  for i in range(n):
    if indegree[i] == 0:
      zeroDegree.put(i)

  while not zeroDegree.empty():
    u = zeroDegree.get()

    result.append(u)

    for v in graph[u]:
      indegree[v] -= 1
      if indegree[v] == 0:
        zeroDegree.put(v)
  # print(result)
  return len(result) == n


def solve():
  n, m = map(int, input().split())

  b = list(map(int, input().split()))

  graph = [[] for i in range(n)]
  for _ in range(m):
    info = input()

    data = None
    i = 0
    j = 0
    if '>' in info:
      data = info.split('>')
      i = int(data[1].strip()) - 1
      j = int(data[0].strip()) - 1
    else:
      data = info.split('<')
      i = int(data[0].strip()) - 1
      j = int(data[1].strip()) - 1
    graph[i].append(j)

  a = []
  if topoSort(graph, a) == False:
    print('NO')
  else:
    print('YES')

    # Compare against B
    print(a)
    print(b)

    A = [0]*n

    for i in a:
      A[i] =

    # a = 1 2 3
    # b = 1 2 3

    # Find the index that a is less than b
    # index = n - 1
    # for i in range(n):
    #   if a[i] > b[i]:
    #     print(a)
    #     return

    #   if a[i] < b[i]:
    #   index = i
    #   break

    # a[index] = b[index] + 1

    # reset values
    # for i in range(index+1, n):
    #   a[i] = 1
    # topo of indices, base 0:

    # a: 1 -> 0 -> 2
      #    1 .  2   3 => [2 1 3]

    # graph
    # 2: [1]
    # 1: [3]
    # 3: []

    # for u in range(n):
    #   arr = graph[u]

    #   # 3 -> 4
    #   # 2 -> 3
    #   for v in arr:
    #     # On the left
    #     # if v > index and a[u] >= a[v]:
    #     #   a[v] = a[u] + 1

    # print(*a)

# a =    1 2 3 4 5 => 1 2 5 x x .   1 2 5 2 2  1 2 5 1 1
# b =    1 2 4 5 5

# ------- 4 x x
# ------- 5 y y


def main():
  t = int(input())

  for i in range(t):
    solve()


main()
