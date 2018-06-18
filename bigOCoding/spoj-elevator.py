line = input()
while not line.strip():
  line = input()
f, s, g, u, d = map(int, line.strip().split())


def bfs(floors, start, goal, up, down):
  path = [-1]*floors
  levels = [None]*floors
  l = 0
  r = 0


  # Start
  # frontier = [start]
  levels[l] = start
  path[start] = 0

  while l <= r:
    u = levels[l]
    for v in [u+up, u-down]:
      if v == goal:
        return path[u] + 1
      if 0 <= v < floors and path[v] == -1:
        # nextLevel.append(v)
        r += 1
        levels[r] = v
        path[v] = path[u] + 1
        
    l += 1
  
  return -1


result = bfs(f, s-1, g-1, u, d)
if result == -1:
  print('use the stairs')
else:
  print(result)
