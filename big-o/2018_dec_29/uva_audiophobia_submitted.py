# https: // uva.onlinejudge.org/index.php?option = com_onlinejudge & Itemid = 8 & page = show_problem & problem = 989
import queue

INF = 10**9


def prim(src, graph, dist, path, visited):
  pq = queue.PriorityQueue()

  dist[src] = 0
  path[src] = -1

  pq.put((0, src))

  while not pq.empty():
    top = pq.get()
    u = top[1]

    # if u == des:
    #   return

    if visited[u]:
      continue

    visited[u] = True

    for w, v in graph[u]:
      if visited[v] == False and dist[v] > w:
        dist[v] = w
        pq.put((w, v))
        path[v] = u


def find_min(src, des, dist, path):
  if des == -1:
    return INF

  if src == des:
    return dist[des]

  d = dist[des]  # want: weight of des -> parent
  # des = 5, parent = 7 -> 40

  parent = path[des]

  d = max(d, find_min(src, parent, dist, path))

  return d


def bfs(src, des, graph):
  n = len(graph)
  visited = [False]*n

  q = queue.Queue()
  q.put(src)
  path = [-1]*n
  visited[src] = True

  while not q.empty():
    u = q.get()

    for v in graph[u]:
      if visited[v] == False:
        q.put(v)
        visited[v] = True
        path[v] = u

      if v == des:
        return path

  return path

# A -> B -> C
# B -> D


def solve(c, s, q, test):
  graph = [[] for i in range(c)]

  for _ in range(s):
    c1, c2, d = map(int, input().split())

    graph[c1-1].append((d, c2-1))
    graph[c2-1].append((d, c1-1))

  print("Case #" + str(test))

  dist = [INF]*c
  path = [-1]*c
  visited = [False]*len(graph)

  for u in range(c):
    if visited[u] == False:
      prim(u, graph, dist, path, visited)  # Q*ElogV E~V^2

  # print(path)
  # print(dist)

  # [-1, 0, 0, 5, -1, 2, -1]

  # Build new graph
  new_graph = [[] for i in range(c)]
  for i, u in enumerate(path):
    if u == -1:
      continue

    new_graph[i].append(u)
    new_graph[u].append(i)

  # print(new_graph)

  for _ in range(q):  # O(Q)
    s, d = map(int, input().split())
    src = s - 1
    des = d - 1

    bfs_path = bfs(src, des, new_graph)  # O(V)
    # print('bfs_path')

    # print(bfs_path)
    min_sound = find_min(src, des, dist, bfs_path)

    if min_sound == INF:
      print("no path")
    else:
      print(min_sound)


test = 0
while True:
  test += 1
  c, s, q = map(int, input().split())
  if c != 0 or s != 0 or q != 0:
    solve(c, s, q, test)
    print()
  else:
    break

# O(Q*SlogC)
# O(E + V) space


# 1 -> 2: 2
# 3 -> 2: 4
# 4 -> 2: 5

# 1,2,3,4,5
# 1 4: ?
# dist = [0,3,1,4,5]
# path = [-1, 2,] # storing parent


#   A ->(50) B -> C(40) ->(30) D : minimum spanning tree
#   B -> E

# # Prove max_edge is the smallest among all the paths
# u -> max_edge_mst -> v
# u -> max_edge_not_mst -> v

# if max_edge_not_mst < max_edge_mst, why not replace max_edge_mst with max_edge_not_mst

# max_edge_mst ? whole tree or one edge?


# A -> B -> E -> G: max_edge_not_mst = 70(BE) . EG

# A -> C -> F -> D -> G: max_edge_mst = 80(DF) .  DG, FG

# A -> C -> F
# A -> B -> E -> G
# D -> G

# replace DF with BE, then going to G through E might be cheaper than from D
# then we still have MST(same value min sum)

# if we use BE, remove DF. sum reduced by 10
# now we use EG: 50
# before we use DG: 40
# sum + 50 - 40 => same sum

# u -> u1 -> u2 -> u3 -> max_edge_mst -> v1 -> v2 -> v3 -> v
