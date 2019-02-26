# https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1541

# dont use 9:   some huge value
# dont use 51: 125
# dont 19: 133
# dont use 31: 121

# O(N*ElogN) 100*100^2*log(100)

import queue

INF = 10**9


def modified_mst(src, graph, excluded_edge):
  n = len(graph)
  dist = [(0, INF)]*n
  visited = [False]*n
  pq = queue.PriorityQueue()

  pq.put((0, src))
  dist[src] = (src, 0)

  while not pq.empty():
    u = pq.get()[1]

    if visited[u]:
      continue

    visited[u] = True

    for w, v in graph[u]:
      if (u, v, w) != excluded_edge and (v, u, w) != excluded_edge and visited[v] == False and dist[v][1] > w:
        pq.put((w, v))

        # Save the u information as well to form the edge later
        dist[v] = (u, w)

  return dist


def calculate_cost(dist):
  min_cost = 0
  for i in range(len(dist)):
    if dist[i][1] != INF:
      min_cost += dist[i][1]
    else:
      return -1
  return min_cost
# 3 3
# # 1 2 1
# 1 2 1
# 2 3 2
# -> 3 3


def main():
  t = int(input())
  for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for i in range(n)]

    for i in range(m):
      a, b, c = map(int, input().split())

      # zero based index
      graph[a-1].append((c, b-1))
      graph[b-1].append((c, a-1))

    # Throw in a fake edge to ignore
    dist = modified_mst(0, graph, ())
    first = calculate_cost(dist)

    # Find the second cheapest
    second = INF
    for i in range(1, n):  # Because d[0] is the edge to itself. so we are not excluding anything
      excluded_edge = (i, dist[i][0], dist[i][1])  # (u,v,w)
      a_dist = modified_mst(0, graph, excluded_edge)
      cost = calculate_cost(a_dist)
      if cost >= first:
        second = min(second, cost)

    print(first, second)


main()

# O(N*MlogN)
