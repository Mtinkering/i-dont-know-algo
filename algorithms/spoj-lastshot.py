'''
' Steven July 3 2018
' https://www.spoj.com/problems/LASTSHOT/
' DFS
'''
import sys
sys.setrecursionlimit(1000000)


class Scanner:
  def __init__(self, istream):
    self.tokenizer = Scanner.__tokenizer__(istream)

  def __tokenizer__(istream):
    try:
      for line in istream:  # line = '2'
        for token in line.strip().split():
          yield token
    except EOFError:
      exit()

  def next(self):
    return self.tokenizer.__next__()


sc = Scanner(sys.stdin)

n = int(sc.next())
m = int(sc.next())

graph = [[] for i in range(n)]
for i in range(m):
  u = int(sc.next())
  v = int(sc.next())

  graph[u-1].append(v-1)


def dfs(graph, src, visited):
  visited[src] = 1
  result = 1

  for v in graph[src]:
    if visited[v] == -1:
      result += dfs(graph, v, visited)

  return result


answer = 0
for i in range(n):
  visited = [-1]*n
  bomb = dfs(graph, i, visited)
  answer = max(answer, bomb)

print(answer)

# O(n(m+n))
