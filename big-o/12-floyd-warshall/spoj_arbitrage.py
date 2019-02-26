# https://www.spoj.com/status/ARBITRAG,entergmode/
def floydWarshall(graph):
  n = len(graph)
 
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if graph[i][k] * graph[k][j] > graph[i][j]:
          graph[i][j] = graph[i][k] * graph[k][j]
        
 
def solve(n):
  
  nameToIndex = {}
  
  for i in range(n):
    nameToIndex[input()] = i
  
  graph = [[0]*n for i in range(n)]
  
  m = int(input())
  
  
#   for i in range(n):
#     graph[i][i] = 1.0
    
  for _ in range(m):
    s = input().strip().split()
    
    u = s[0]
    v = s[2]
    w = float(s[1])
    
    if graph[nameToIndex[u]][nameToIndex[v]] < w:
      graph[nameToIndex[u]][nameToIndex[v]] = w
 
#       USD SGD VND
  
#   USD  1
#   SGD      1
#   VND          2
 
  
  floydWarshall(graph)
  
  
  for i in range(n):
    if graph[i][i] > 1:
      return 'Yes'
 
  return 'No'  
 
t = 1
while True:
  n = int(input())
  
  if n == 0:
    break
    
  ans = solve(n)
  input()
  
  print('Case %d: %s' % (t, ans))
  
  t += 1