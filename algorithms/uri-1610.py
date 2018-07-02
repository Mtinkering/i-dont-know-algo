'''
' Steven June 30 2018
' https: // www.urionlinejudge.com.br/judge/en/problems/view/1610
' DFS. Detect a cycle in the graph => detect the back edge
'''

import sys
sys.setrecursionlimit(1000000)


def readInput():
  line = input().strip()
  while not line:
    line = input().strip()
  return line


t = int(readInput())

# A -> B -> C -> E -> B
# D -> B
#   visited[src] = 0 # not visited
#                  1 # visiting
#                  2 # visited


def dfs(graph, src, visited):
  visited[src] = 1
  for u in graph[src]:
    if visited[u] == 0:
      if dfs(graph, u, visited):
        return True
    elif visited[u] == 1:
      return True
  visited[src] = 2
  return False


def hasLoop(graph):
  n = len(graph)

  visited = [0 for i in range(n)]
  for i in range(n):
    if visited[i] == 0:
      if dfs(graph, i, visited) == True:
        return True
  return False


def solve():
  n, m = map(int, readInput().split())

  graph = [[] for i in range(n)]

  for _ in range(m):
    u, v = map(int, readInput().split())
    if v-1 not in graph[u-1]:
      graph[u-1].append(v-1)

  print('NAO' if hasLoop(graph) == False else 'SIM')


for _ in range(t):
  solve()
