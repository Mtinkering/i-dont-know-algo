# https: // leetcode.com/problems/friend-circles/
# Disjoint set union
# Try with BFS?
# O(n^2) in space and time. Due to using path compression and union by rank


class Solution:
  def findCircleNum(self, M):
    def bfs(i, M, visited):
      visited[i] = True

      layer = [i]

      while len(layer) != 0:
        tmp = []

        for u in layer:
          for v, val in enumerate(M[u]):
            if not visited[v] and val == 1:
              visited[v] = True
              tmp.append(v)

        layer = tmp

    n = len(M)
    visited = [False]*n

    counter = 0
    for i in range(n):
      if not visited[i]:
        bfs(i, M, visited)
        counter += 1

    return counter

# Disjoint set union
# DFS
  def findCircleNum(self, M):
    def dfs(i, M, visited):
      visited[i] = True

      for v, val in enumerate(M[i]):
        if not visited[v] and val == 1:
          visited[v] = True
          dfs(v, M, visited)

    n = len(M)
    visited = [False]*n

    counter = 0
    for i in range(n):
      if not visited[i]:
        dfs(i, M, visited)
        counter += 1

    return counter
