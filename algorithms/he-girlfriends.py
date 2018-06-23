'''
' Steven June 20 2018
' https: // www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bishu-and-his-girlfriend/
' BFS, DFS
'''

def dfs(graph, src):
  # Use the stack
  visited = [-1]*len(graph)
  st = []

  st.append(src)
  visited[src] = 0

  # DFS
  while len(st) != 0:
    u = st.pop()

    for v in graph[u]:
      if visited[v] == -1:
        st.append(v)
        visited[v] = visited[u] + 1

  return visited

n = int(input())

graph = [[] for i in range(n)]

for i in range(n-1):
  u, v = map(int, input().split())
  graph[u-1].append(v-1)
  graph[v-1].append(u-1)

visited = dfs(graph, 0)

q = int(input())

arr = []
for i in range(q):
  g = int(input())

  # We want to keep track of the distance and the id
  arr.append((visited[g-1], g))

minDistance = n + 1
minId = n + 1

for distance in arr:
  if distance[0] <= minDistance:
    minDistance = distance[0]
    minId = min(minId, distance[1])

# First one, with the id is the answer
print(minId)
