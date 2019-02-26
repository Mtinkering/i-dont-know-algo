
# Union by rank and path compression: this is the best optimization for the implementation
#
# The problem from the beginning of the article is solvable in O(N + M)
# and O(N) for memory using disjoint-set data structure,
# where N is the number of persons and M is the number of friendships
#
# The difference for time execution is not big if the problem is solved with BFS,
# but we don’t need to keep in memory the vertices of the graph.
# Let’s see if the problem was like: In a room are N persons and you had to handle Q queries.
# A query is of the form “x y 1, ” meaning that x is friends with y, or “x y 2” meaning
# that we are asked to output if x and y are in same group of friends at that moment in time.
# In this case the solution with disjoint-set data structure is the fastest,
# giving a complexity of O(N + Q), => which means finding while adding more edges.
# Also dont have to store the whole graph
# Recall: BFS O(M+N) in time and space

# Complexity of using disjoint set for each operation ~ amortized: O(alpha(n)) ~ O(1)
# So for M operation, O(M)
# Total: O(m + n) or O(n + q)
# Remember we don't allow deletion
# Only merge, create and find


def unionSet(u, v, parent, size):
  up = findSet(u, parent, size)
  vp = findSet(v, parent, size)

  if up == vp:
    return

  if size[up] > size[vp]:
    parent[vp] = up
    size[up] = size[up] + size[vp]
  else:
    parent[up] = vp
    size[vp] = size[vp] + size[up]


def findSet(u, parent, size):
  if parent[u] == u:
    return u

  parent[u] = findSet(parent[u], parent, size)

  return parent[u]


def main():
  n, m = map(int, input().split())

  parent = [i for i in range(n)]
  size = [1 for i in range(n)]

  for i in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())

    unionSet(u, v, parent, size)

  ans = []
  for i in range(n):
    p = findSet(i, parent, size)
    ans.append(size[p] - 1)

  print(*ans)


main()
# Problems:
# 1. How to find if 2 persons are in the same group or not
